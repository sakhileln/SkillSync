"""A module for helper functions."""

from collections import OrderedDict
from datetime import datetime as dt
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


# pylint: disable=redefined-outer-name
def sign_up_with_email_and_password(email: str, password: str) -> Dict[str, Any]:
    """
    Handle user sign up using email and password using Firebase Authentication.

    params: email-> str: Email for the user
    params: password-> str: Password for the account

    Return-> json: JSON information about the request whether successful or not.
    """
    payload = json.dumps(
        {"email": email, "password": password, "returnSecureToken": True}
    )
    response = requests.post(
        rest_api_url_sign,
        params={"key": FIREBASE_WEB_API_KEY},
        data=payload,
        timeout=10,
    )
    return response.json()


def sign_in_with_email_and_password(email: str, password: str) -> Dict[str, Any]:
    """
    Handle user sign in using email and password using Firebase Authentication.

    params: email-> str: Email for the user
    params: password-> str: Password for the account

    Return-> json: JSON information about the request whether successful or not.
    """
    payload = json.dumps(
        {"email": email, "password": password, "returnSecureToken": True}
    )
    response = requests.post(
        rest_api_url_log, params={"key": FIREBASE_WEB_API_KEY}, data=payload, timeout=10
    )
    return response.json()


def sign_up() -> None:
    """Function to prompt user for signing up to the application."""
    # pylint: disable=redefined-outer-name
    email = input("Please enter your email: ")
    password = pwinput(prompt="Please enter your password: ")
    response = sign_up_with_email_and_password(email, password)
    if "error" in response:
        cprint("Sign up failed.", "red")
    else:
        cprint("Sign up successfull. Cool beans!!!", "green")


def sign_in() -> None:
    """Function to handle signing into the application."""
    # pylint: disable=redefined-outer-name
    email = input("Please enter your email: ")
    password = pwinput(prompt="Please enter your password: ")
    response = sign_in_with_email_and_password(email, password)
    if "error" in response:
        cprint("Log in failed.", "red")
    else:
        cprint("Log in successfull. Yay!!!", "green")


# Helper function
def print_workshops(workshops: OrderedDict[str, str]) -> None:
    """
    Print user workshops in a friendly manner.

    params: workshops-> OrderedDict: Workshops for sepcific mentor or mentee.

    Return: None
    """
    # pylint: disable=pointless-string-statement
    """
    date_requested: 2025-01-13T22:22:08.923426
    requestor_id: 3
    topic: Python Data Structures
    """
    for key, val in workshops.items():
        if key == "date_requested":
            date, timez = val.split("T")
            y, m, d = (
                int(date.split("-")[0]),
                int(date.split("-")[1]),
                int(date.split("-")[2]),
            )
            hour, minute, sec = list(map(int, timez[:8].split(":")))
            date_obj = dt(y, m, d, hour, minute, sec)
            print("Booking Date: ", end="")
            # pylint: disable=line-too-long
            print(
                f"{date_obj.strftime('%A')}, {date_obj.strftime('%d')} {date_obj.strftime('%B')}, {date_obj.strftime('%Y')}"
            )
            print(f"Time: {date_obj.strftime('%X')}")
        elif key == "topic":
            print(f"Topic: {val}")
        else:
            continue


# Example usage
if __name__ == "__main__":
    # pylint: disable=redefined-outer-name
    email = input("Enter email: ")
    password = input("Enter password: ")
    # result = sign_up_with_email_and_password(email, password)
    # result = sign_in_with_email_and_password(email, password)
    # print(result)
    sign_up()
