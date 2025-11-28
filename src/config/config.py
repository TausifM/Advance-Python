import os
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables from a .env file
load_dotenv()

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://tanmayagrawwal_db_user:7vzPPNjVJ055YlKh@cluster0.l90eely.mongodb.net/")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "ecommerce_db")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "TestSecretKey12345")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 15)))
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", 30)))

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads/images/")