from motor.motor_asyncio import AsyncIOMotorClient
from config.config import MONGO_DB_URI, MONGO_DB_NAME

client = AsyncIOMotorClient(MONGO_DB_URI)
db = client[MONGO_DB_NAME]