from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

DB_NAME="rem"
MONGO_DB_URI ="mongodb+srv://rem:rem@cluster0.2n0gz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

mongo = MongoClient(MONGO_DB_URI)
dbname = mongo[DB_NAME]
