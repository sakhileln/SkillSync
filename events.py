"""
This script provides functionality to authenticate with Google Calendar API 
and create a calendar event via a terminal script. The event includes a description, 
start/end times, and invites a specified attendee. Authentication is managed using 
OAuth 2.0, with credentials stored for subsequent runs.
"""

import datetime
import os
import os.path
import pickle

# pylint: disable=ungrouped-imports
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
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


def get_events():
    """
    Module that prints the start and name of the next 10 events on the user's calendar
    using Google Calendar API.
    """
    try:
        service = build("calendar", "v3", credentials=authenticate_google())

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        print("Getting the upcoming 10 events")
        # pylint: disable=no-member
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])

    except HttpError as error:
        print(f"An error occurred: {error}")


def delete_event(event_id):
    """Delete a specific event by its Google Calendar event ID"""
    try:
        service = build("calendar", "v3", credentials=authenticate_google())
        # pylint: disable=no-member
        service.events().delete(calendarId="primary", eventId=event_id).execute()
        cprint(f"Event {event_id} deleted successfully!", "green")
    # pylint: disable=broad-exception-caught
    except Exception as error:
        cprint(f"An error occurred: {error}", "red")


def get_event_id(calendar_id="primary", event_summary=None):
    """Retrieve event ID by summary or list all events"""
    service = build("calendar", "v3", credentials=authenticate_google())
    # pylint: disable=no-member
    events_result = service.events().list(calendarId=calendar_id).execute()
    events = events_result.get("items", [])

    if event_summary:
        for event in events:
            if event["summary"] == event_summary:
                return event["id"]

    return events  # Return all events if no specific summary provided


if __name__ == "__main__":
    # create_event("sakhilelindah@gmail.com")
    # delete_event("Quick SkillSync Meeting")
    # print(get_event_id(event_summary="Quick SkillSync Meeting"))
    get_events()
