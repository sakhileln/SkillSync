import datetime

from google.oauth2 import service_account
from googleapiclient.discovery import build


def create_event(attandee_email: str) -> None:
    # Load service account credentials
    SERVICE_ACCOUNT_FILE = 'skillsync-firebase-adminsdk.json'
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    # Authenticate using service account
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    # Build Google Calendar service
    service = build('calendar', 'v3', credentials=credentials)

    # Event Details
    event = {
        'summary': 'Test Event',
        'location': 'Online',
        'description': 'A test event added via API',
        'start': {
            'dateTime': '2025-01-22T16:00:00+02:00',  # SA time offset
            'timeZone': 'Africa/Johannesburg',
        },
        'end': {
            'dateTime': '2025-01-22T17:00:00+02:00',  # Duration: 1 hour
            'timeZone': 'Africa/Johannesburg',
        },
        'attendees': [
            { 'email': attandee_email },
        ],
    }

    # Insert the event into the calendar
    calendar_id = 'primary'
    event_result = service.events().insert(calendarId=calendar_id, body=event).execute()

    return event_result.get("htmlLink")


if __name__ == "__main__":
    print(f'Event created: { create_event("sakhilelindah@gmail.com") }')
