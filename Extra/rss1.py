from typing import Dict, List, Union
from FallenRobot import MONGO_DB_URI as MONGO_URL
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
aiosession = ClientSession()
mongo_client = MongoClient(MONGO_URL)
db = mongo_client.rem
rssdb = db.rss

async def get_http_status_code(url: str) -> int:
    async with aiosession.head(url) as resp:
        return resp.status

async def add_rss_feed(chat_id: int, url: str, last_title: str):
    return await rssdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"url": url, "last_title": last_title}},
        upsert=True,
    )


async def remove_rss_feed(chat_id: int):
    return await rssdb.delete_one({"chat_id": chat_id})


async def update_rss_feed(chat_id: int, last_title: str):
    return await rssdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"last_title": last_title}},
        upsert=True,
    )


async def is_rss_active(chat_id: int) -> bool:
    return await rssdb.find_one({"chat_id": chat_id})


async def get_rss_feeds() -> list:
    data = []
    async for feed in rssdb.find({"chat_id": {"$exists": 1}}):
        data.append(
            dict(
                chat_id=feed["chat_id"],
                url=feed["url"],
                last_title=feed["last_title"],
            )
        )
    return data


async def get_rss_feeds_count() -> int:
    return len([i async for i in rssdb.find({"chat_id": {"$exists": 1}})])
  
