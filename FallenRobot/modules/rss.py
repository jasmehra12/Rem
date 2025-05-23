from asyncio import get_event_loop, sleep

from feedparser import parse
from pyrogram import filters
from pyrogram.errors import (
    ChannelInvalid,
    ChannelPrivate,
    InputUserDeactivated,
    UserIsBlocked,
)
from pyrogram.types import Message
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from FallenRobot import pbot as app, LOGGER as log, MONGO_DB_URI as MONGO_URL
from FallenRobot.events import capture_err
from Extra.rss1 import (
    add_rss_feed,
    get_rss_feeds,
    is_rss_active,
    remove_rss_feed,
    update_rss_feed,
    get_http_status_code,
)
from FallenRobot.events import get_urls_from_text
from Extra.rss import Feed

mongo_client = MongoClient(MONGO_URL)
db = mongo_client.rem
RSS_DELAY = 70
rssdb = db.rss

__mod_name__ = "Rꜱꜱ"
__help__ = """
/add_feed [URL] - Add a feed to chat
/rm_feed - Remove feed from chat

**Note:**
    - This will check for updates every {RSS_DELAY // 60} minutes.
    - You can only add one feed per chat.
    - Currently RSS and ATOM feeds are supported.
"""


async def rss_worker():
    log.info("RSS Worker started")
    while not await sleep(RSS_DELAY):
        feeds = await get_rss_feeds()
        if not feeds:
            continue

        loop = get_event_loop()

        for _feed in feeds:
            chat = _feed["chat_id"]
            try:
                url = _feed["url"]
                last_title = _feed.get("last_title")

                parsed = await loop.run_in_executor(None, parse, url)
                feed = Feed(parsed)

                if feed.title == last_title:
                    continue

                await app.send_message(
                    chat, feed.parsed(), disable_web_page_preview=True
                )
                await update_rss_feed(chat, feed.title)
            except (
                ChannelInvalid,
                ChannelPrivate,
                InputUserDeactivated,
                UserIsBlocked,
                AttributeError,
            ):
                await remove_rss_feed(chat)
                log.info(f"Removed RSS Feed from {chat} (Invalid Chat)")
            except Exception as e:
                log.info(f"RSS in {chat}: {str(e)}")


loop = get_event_loop()
loop.create_task(rss_worker())


@app.on_message(filters.command("add_feed"))
@capture_err
async def add_feed_func(_, m: Message):
    if len(m.command) != 2:
        return await m.reply("Read 'RSS' section in help menu.")
    url = m.text.split(None, 1)[1].strip()

    if not url:
        return await m.reply("[ERROR]: Invalid Argument")

    urls = get_urls_from_text(url)
    if not urls:
        return await m.reply("[ERROR]: Invalid URL")

    url = urls[0]
    status = await get_http_status_code(url)
    if status != 200:
        return await m.reply("[ERROR]: Invalid Url")

    ns = "[ERROR]: This feed isn't supported."
    try:
        loop = get_event_loop()
        parsed = await loop.run_in_executor(None, parse, url)
        feed = Feed(parsed)
    except Exception:
        return await m.reply(ns)
    if not feed:
        return await m.reply(ns)

    chat_id = m.chat.id
    if await is_rss_active(chat_id):
        return await m.reply("[ERROR]: You already have an RSS feed enabled.")
    try:
        await m.reply(feed.parsed(), disable_web_page_preview=True)
    except Exception:
        return await m.reply(ns)
    await add_rss_feed(chat_id, parsed.url, feed.title)


@app.on_message(filters.command("rm_feed"))
async def rm_feed_func(_, m: Message):
    if await is_rss_active(m.chat.id):
        await remove_rss_feed(m.chat.id)
        await m.reply("Removed RSS Feed")
    else:
        await m.reply("There are no active RSS Feeds in this chat.")
