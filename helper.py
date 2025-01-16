"""A module for helper functions."""

import os
import json
from typing import Dict, Any

import requests
from pwinput import pwinput
from termcolor import cprint

from dotenv import load_dotenv

load_dotenv()

FIREBASE_WEB_API_KEY = os.getenv("FIREBASE_API_KEY")
# pylint: disable=invalid-name
rest_api_url_sign = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
rest_api_url_log = (
    "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
)


def sign_up_with_email_and_password(email: str, password: str) -> Dict[str, Any]:
    payload = json.dumps(
        {"email": email, "password": password, "returnSecureToken": True}
    )
    response = requests.post(
        rest_api_url_sign, params={"key": FIREBASE_WEB_API_KEY}, data=payload
    )
    return response.json()


def sign_in_with_email_and_password(email: str, password: str) -> Dict[str, Any]:
    payload = json.dumps(
        {"email": email, "password": password, "returnSecureToken": True}
    )
    response = requests.post(
        rest_api_url_log, params={"key": FIREBASE_WEB_API_KEY}, data=payload
    )
    return response.json()


def sign_up() -> None:
    email = input("Please enter your email: ")
    passord = pwinput(prompt="Please enter your password: ")
    response = sign_up_with_email_and_password(email, password)
    if "error" in response:
        cprint("Sign up failed.", "red")
    else:
        cprint("Sign up successfull. Cool beans!!!", "green")


def sign_in() -> None:
    email = input("Please enter your email: ")
    passord = pwinput(prompt="Please enter your password: ")
    response = sign_in_with_email_and_password(email, password)
    if "error" in response:
        cprint("Log in failed.", "red")
    else:
        cprint("Log in successfull. Yay!!!", "green")


# Example usage
if __name__ == "__main__":
    email = input("Enter email: ")
    password = input("Enter password: ")
    # result = sign_up_with_email_and_password(email, password)
    # result = sign_in_with_email_and_password(email, password)
    # print(result)
    sign_up()
