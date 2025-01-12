import os

import firebase_admin
from firebase_admin import credentials

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": DATABASE_URL})

