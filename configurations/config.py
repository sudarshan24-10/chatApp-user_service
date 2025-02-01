import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = int(os.getenv("PORT", 5000))
    
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Select config based on environment
config = DevelopmentConfig() if os.getenv("DEBUG") == "true" else ProductionConfig()
