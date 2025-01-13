import os

import pyrebase
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# configuration
config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("DATABASE_URL"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
}

# Initialize Pyrebase
firebase = pyrebase.initialize_app(config)

db = firebase.database()

# Create a new user
def create_user(user_id, name, email, role, expertise):
    user_data = {
        'name': name,
        'email': email,
        'role': role,
        'expertise': expertise
    }
    db.child("users").child(user_id).set(user_data)

# Read a user by ID
def read_user(user_id):
    return db.child("users").child(user_id).get().val()


if __name__ == "__main__":
    # create_user(1, "Sakhile", "sakhi@example.com", "mentee", "Python")
    print(read_user(1))
