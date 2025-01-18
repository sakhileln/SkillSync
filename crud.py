"""Module to handle the CRUD opertations."""

import os
import datetime

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


# pylint: disable=redefined-outer-name
def create_user(user_id, name, email, role, expertise):
    """Create a new user."""
    user_data = {"name": name, "email": email, "role": role, "expertise": expertise}
    db.child("users").child(user_id).set(user_data)


# pylint: disable=redefined-outer-name
def read_user(user_id):
    """Read a user by ID"""
    return db.child("users").child(user_id).get().val()


def read_users():
    """Read a users from database."""
    return db.child("users").get().val()


def find_user(username):
    """Find a user by email and return their ID."""
    users = read_users()

    for item in users:
        if not isinstance(item, dict):
            continue

        for user_id, user_info in item.items():
            if user_info == username:
                return item["email"]  # Return the user's ID if found
    return None  # Return None if no matching user is found


# pylint: disable=redefined-outer-name
def update_user(user_id, name=None, email=None, role=None, expertise=None):
    """Update a user's information"""
    updates = {}
    if name:
        updates["name"] = name
    if email:
        updates["email"] = email
    if role:
        updates["role"] = role
    if expertise:
        updates["expertise"] = expertise

    db.child("users").child(user_id).update(updates)


# pylint: disable=redefined-outer-name
def delete_user(user_id):
    """Delete user by id."""
    db.child("users").child(user_id).remove()


def create_meeting(meeting_id, mentor_id, mentee_id, time, status="Scheduled"):
    """Create a new meeting"""
    meeting_data = {
        "mentor_id": mentor_id,
        "mentee_id": mentee_id,
        "time": time,
        "status": status,
    }
    db.child("meetings").child(meeting_id).set(meeting_data)


def read_meeting(meeting_id):
    """Read a meeting by ID."""
    return db.child("meetings").child(meeting_id).get().val()


def update_meeting(meeting_id, status=None, time=None):
    """Update a meeting's status or time."""
    updates = {}
    if status:
        updates["status"] = status
    if time:
        updates["time"] = time

    db.child("meetings").child(meeting_id).update(updates)


def delete_meeting(meeting_id):
    """Delete a meeting by ID"""
    db.child("meetings").child(meeting_id).remove()


def create_workshop(workshop_id, requestor_id, topic):
    """Create a new workshop."""
    workshop_data = {
        "requestor_id": requestor_id,
        "topic": topic,
        "date_requested": datetime.datetime.utcnow().isoformat(),
    }
    db.child("workshops").child(workshop_id).set(workshop_data)


def read_workshop(workshop_id):
    """Read a workshop by ID."""
    return db.child("workshops").child(workshop_id).get().val()


def update_workshop(workshop_id, topic=None):
    """Update a workshop's topic or requestor ID"""
    updates = {}
    if topic:
        updates["topic"] = topic

    db.child("workshops").child(workshop_id).update(updates)


def delete_workshop(workshop_id):
    """Delete a workshop by ID."""
    db.child("workshops").child(workshop_id).remove()


if __name__ == "__main__":
    # create_user(2, "Kyle", "kyle@dsquad.co.za", "mentor", "Python")
    # print(read_user(1))
    # create_meeting(1, 3, 4, "09:30")
    # print(read_meeting(1))
    # create_workshop(1, 3, "Python Data Structures")
    # print(read_workshop(1))
    # print(read_users())
    # pylint: disable=invalid-name
    user_email_to_search = "Kyle"
    user_id = find_user(user_email_to_search)

    if user_id:
        print(f"User ID for {user_email_to_search}: {user_id}")
    else:
        print(f"No user found with email: {user_email_to_search}")
