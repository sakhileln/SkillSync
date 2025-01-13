import os

import pyrebase
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Firebase configuration
config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("DATABASE_URL"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
}

# Initialize Pyrebase
firebase = pyrebase.initialize_app(config)

db = firebase.database()

# Create a new entry in the root node (example)
data = {"name": "Ndlazi", "meetings": 3}
db.child("root").set(data)

# Retrieve data from root node
root_data = db.child("root").get()
print(root_data.val())  # Print the retrieved data

# Update operation
db.child("root").update({"name": "Updated Name"})
updated_data = db.child("root").get()
print(updated_data.val())  # Print updated data

# Set operation (overwrites existing data)
db.child("meetings").set(5)  # Set meetings to 5
meetings_data = db.child("meetings").get()
print(meetings_data.val())  # Print meetings data
