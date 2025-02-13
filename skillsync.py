"""MAin driver module for the program."""

import os

import click
from termcolor import cprint

from booking_system import bookings
from crud import read_workshop, read_meeting, find_user, create_user, create_meeting
from events import get_events, create_event, get_event_id, delete_event
from helper import (
    print_workshops,
    sign_in_with_email_and_password,
    sign_up_with_email_and_password,
)

# Simulate in-memory session storage
session = {}


def login_required(func):
    """Decorstor to enforce login before accessing a command."""

    # pylint: disable=inconsistent-return-statements
    def wrapper(*args, **kwargs):
        """Need to find a way to hide you on the CLI."""
        if "user" not in session:
            click.echo("Error: You must log in to perform this action.")
            return
        return func(*args, **kwargs)

    return wrapper


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli():
    """A Python-based Command-Line Interface (CLI) application for managing workshop bookings
    and one-on-one meetings."""


@cli.command()
@click.option(
    "--email",
    "-e",
    prompt="Please enter your email",
    required=True,
    help="Email of a registered user.",
)
@click.option(
    "--password",
    "-p",
    prompt="Please enter your password",
    required=True,
    help="Password of a registered user.",
)
def login(email, password):
    """Log in to the application."""
    # sign_in()
    # Simulate successful login
    # if email == "sakhi@example.com" and password == "kode":
    #     session["user"] = email
    #     click.echo("Login successful!")
    # else:
    #     click.echo("Invalid email or password. Please try again.")

    response = sign_in_with_email_and_password(email, password)
    if "error" in response:
        cprint("Log in failed.", "red")
    else:
        cprint("Log in successful. Yay!!!", "green")


@cli.command()
@click.option(
    "--email",
    "-e",
    prompt="Please enter your email",
    required=True,
    help="New user email.",
)
@click.option(
    "--password",
    "-p",
    prompt="Please enter your password",
    required=True,
    help="New user password.",
)
# pylint: disable=function-redefined, no-value-for-parameter
def sign_up(email, password):
    """Add new user to application."""
    response = sign_up_with_email_and_password(email, password)
    if "error" in response:
        cprint("Sign up failed.", "red")
    else:
        create_user(2, "Kyle", email, "Mentor", "DevOps")
        cprint("Sign up successful. Cool beans!!!", "green")
    print(f"{email}, {password}")


@cli.command()
# @login_required
def view_workshops():
    """List upcoming workshops and mentors available for booking."""
    click.echo("Lissing upcoming workshops: ")
    workshops = read_workshop(1)
    get_events()
    click.echo(print_workshops(workshops))


# @login_required
@cli.command()
@click.option(
    "--mentor",
    "-m",
    prompt="Mentor Name",
    required=True,
    help="The name of the mentor.",
)
@click.option(
    "--time",
    "-t",
    prompt="Time",
    required=True,
    help="Time of the meeting.",
)
def request_meeting(mentor, time):
    """Request a mentor or peer session."""
    # create_meeting(2, 1, 4, "10:15")
    # May have to create meeting using emails as IDs

    # Take mentor name, read user database, get user id for the mentor
    user_email = find_user(mentor)
    if user_email is None:
        cprint("Could not find mentor or mentee. Please try again.", "red")
    else:
        ...
        # Booking system should handle the slots and times
        bookings()
        create_event(user_email)
        create_meeting(2, 2, 1, time)
        # User the email and time to create the meeting on the database

    cprint(f"Meeting request sent to mentor: {mentor} for {time}", "green")
    # click.echo(f"Meeting request sent to mentor: {mentor} at {time}")


@cli.command()
def view_bookings():
    """Display a list of all confirmed bookings."""
    read_workshop(1)
    read_meeting(1)


@cli.command()
@click.option(
    "--title",
    "-t",
    help="Name of meeting/booking you would like to cancel.",
    required=True,
    prompt="Meeting Title",
)
def cancel_booking(title):
    """Allow users to cancel an existing booking."""
    # pylint: disable=invalid-name
    meeting_eventId = get_event_id(title)
    # Handle unexpected output
    delete_event(meeting_eventId)
    # Must be used when successfully retrieved meeting_eventID


@cli.command()
def logout():
    """Log out of your account."""
    if os.path.exists("token.pickle"):
        os.remove("token.pickle")
        cprint("Logged out successfully", "green")
        click.echo("Logged out successfully.")
    else:
        cprint("You are not logged in.", "red")
        click.echo("You are not logged in.")


if __name__ == "__main__":
    cli()
    # od = OrderedDict([
    #          ('date_requested', '2025-01-13T22:22:08.923426'),
    #          ('requestor_id', 3),
    #          ('topic', 'Python Data Structures')
    # ])
    # print_workshops(od)
    # date, tm = "2025-01-13T22:22:08.923426".split("T")
    # print(date, tm[:5])
