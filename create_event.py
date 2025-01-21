"""
This script provides functionality to authenticate with Google Calendar API 
and create a calendar event via a terminal script. The event includes a description, 
start/end times, and invites a specified attendee. Authentication is managed using 
OAuth 2.0, with credentials stored for subsequent runs.
"""

import os
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from termcolor import cprint


# Scopes for Google Calendar API
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def authenticate_google():
    """Authenticate Google account for Google Calendar API."""
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return creds


def create_event(email):
    """Creates a calendar event and invites the given email."""
    service = build("calendar", "v3", credentials=authenticate_google())

    # Define event details
    event = {
        "summary": "Quick SkillSync Meeting",
        "location": "Virtual",
        "description": "Sync-up meeting to discuss progress.",
        "start": {
            "dateTime": "2025-01-22T10:00:00+02:00",  # SA time offset
            "timeZone": "Africa/Johannesburg",
        },
        "end": {
            "dateTime": "2025-01-22T11:00:00+02:00",  # Duration: 1 hour
            "timeZone": "Africa/Johannesburg",
        },
        "attendees": [
            {"email": email},
        ],
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 24 * 60},  # 24 hours before
                {"method": "popup", "minutes": 10},  # 10 minutes before
            ],
        },
    }

    # Insert the event
    # pylint: disable=no-member
    event = (
        service.events()
        .insert(calendarId="primary", body=event, sendUpdates="all")
        .execute()
    )
    cprint(
        f"Event created successfully! View it here: {event.get('htmlLink')}", "green"
    )


def delete_event(eventId) -> None:
    service = build("calendar", "v3", credentials=authenticate_google())
    service.events().delete(calendarId='primary', eventId=eventId).execute()

if __name__ == "__main__":
    # Test with one email
    # create_event("sakhilelindah@gmail.com")
    delete_event("Quick SkillSync Meeting")
