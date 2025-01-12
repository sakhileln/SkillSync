import os

import firebase_admin
from firebase_admin import db, credentials

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": DATABASE_URL})

# Creating reference to root node
ref = db.reference("/")

# Retrieving data from root node
ref.get()
db.reference("/name").get()

# Set operation
db.reference("/meetings").set(3)
ref.get()

# Update operation
db.reference("/").update({"name": "Ndlazi"})
ref.get()