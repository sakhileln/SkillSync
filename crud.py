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

def create_user(user_id, name, email, role, expertise):
    """Create a new user."""
    user_data = {
        'name': name,
        'email': email,
        'role': role,
        'expertise': expertise
    }
    db.child("users").child(user_id).set(user_data)


def read_user(user_id):
    """Read a user by ID"""
    return db.child("users").child(user_id).get().val()

def update_user(user_id, name=None, email=None, role=None, expertise=None):
    """Update a user's information"""
    updates = {}
    if name:
        updates['name'] = name
    if email:
        updates['email'] = email
    if role:
        updates['role'] = role
    if expertise:
        updates['expertise'] = expertise
    
    db.child("users").child(user_id).update(updates)


def delete_user(user_id):
    """Delete user by id."""
    db.child("users").child(user_id).remove()


def create_meeting(meeting_id, mentor_id, mentee_id, time, status="Scheduled"):
    """Create a new meeting"""
    meeting_data = {
        'mentor_id': mentor_id,
        'mentee_id': mentee_id,
        'time': time,
        'status': status
    }
    db.child("meetings").child(meeting_id).set(meeting_data)


def read_meeting(meeting_id):
    """Read a meeting by ID."""
    return db.child("meetings").child(meeting_id).get().val()


if __name__ == "__main__":
    # create_user(1, "Sakhile", "sakhi@example.com", "mentee", "Python")
    print(read_user(1))
