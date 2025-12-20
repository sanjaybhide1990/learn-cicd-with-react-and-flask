# Environment configurations

import os
from dotenv import load_dotenv

class Config: 
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    database = os.getenv('DB_NAME')

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@{host}/{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False