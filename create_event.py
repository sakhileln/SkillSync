from google.oauth2 import service_account
from googleapiclient.discovery import build


def create_event(attendee_email: str, sender: str):
    # Path to your service account JSON key file
    SERVICE_ACCOUNT_FILE = 'skillsync-firebase-adminsdk.json'
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    # Authenticate using the service account and impersonate a user
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES,
        subject=sender
    )

    # Build the Google Calendar API service
    service = build('calendar', 'v3', credentials=credentials)

    # Define the event details
    event = {
        "summary": "Test Meeting with Attendee",
        "location": "Online",
        "description": "A scheduled meeting created via Google Calendar API.",
        "start": {
            "dateTime": "2025-01-22T16:00:00+02:00",  # SA time offset
            "timeZone": "Africa/Johannesburg",
        },
        "end": {
            "dateTime": "2025-01-22T17:00:00+02:00",  # Duration: 1 hour
            "timeZone": "Africa/Johannesburg",
        },
        "attendees": [
            {"email": attendee_email},
        ],
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 24 * 60},  # Email reminder: day before
                {"method": "popup", "minutes": 10},       # Popup reminder: 10 minutes before
            ],
        },
    }

    # Insert the event into the primary calendar of the impersonated user
    calendar_id = 'primary'
    event_result = service.events().insert(calendarId=calendar_id, body=event).execute()

    print(f'Event created: {event_result.get("htmlLink")}')




if __name__ == "__main__":
    create_event("sakhilelindah@gmail.com", "sakhilelindah@gmail.com")
