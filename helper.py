"""A module for helper functions."""

import firebase_admin
from firebase_admin import auth, credentials

# Initialize Firebase Amdin SDK
cred = credentials.Certificate("")
firebase_admin.initialize_app(cred)

def create_user_with_email_and_password(email: str, password: str) -> None:
    try:
        # Create a new user with email and password
        user = auth.create_user(
            email=email,
            password=password
        )
        print(f"Successfully created new user: {user.uid}")
    except firebase_admin.auth.AuthError as e:
        print(f"Error creating user: {e}")

if __name__ == "__main__":
    # Example usage
    email = "user@example.com"
    password = "very_strong_password"
    create_user_with_email_and_password(email, password)