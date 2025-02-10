from Database.mongodb.db import *

nekomodedb = dbname.nekomode

async def is_nekomode_on(chat_id: int) -> bool:
    chat = await nekomodedb.find_one({"chat_id_toggle": chat_id})
    return not bool(chat)


async def nekomode_on(chat_id: int):
    await nekomodedb.delete_one({"chat_id_toggle": chat_id})


async def nekomode_off(chat_id: int):
    await nekomodedb.insert_one({"chat_id_toggle": chat_id})
