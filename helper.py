"""A module for helper functions."""

import os

import requests
import json

from dotenv import load_dotenv

load_dotenv()

FIREBASE_WEB_API_KEY = os.getenv("apiKey")
rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"

def sign_up_with_email_and_password(email, password):
    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": True
    })
    response = requests.post(rest_api_url, params={"key": FIREBASE_WEB_API_KEY}, data=payload)
    return response.json()

# Example usage
if __name__ == "__main__":
    email = input("Enter email: ")
    password = input("Enter password: ")
    result = sign_up_with_email_and_password(email, password)
    print(result)
