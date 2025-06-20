from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

DB_NAME="Mehra"
MONGO_DB_URI ="mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

mongo = MongoClient(MONGO_DB_URI)
dbname = mongo[DB_NAME]
