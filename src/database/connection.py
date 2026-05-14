from motor.motor_asyncio import AsyncIOMotorClient
from config.config import MONGO_DB_URI, MONGO_DB_NAME
import certifi

client = AsyncIOMotorClient(
    MONGO_DB_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    tlsAllowInvalidCertificates=True
)

db = client[MONGO_DB_NAME]

print("MongoDB Connected")