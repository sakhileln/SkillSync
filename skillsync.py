import click

from helper import sign_in, sign_up


# Simulate in-memory session storage
session = {}


def login_required(func):
    """Decorstor to enforce login before accessing a command."""
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            click.echo("Error: You must log in to perform this action.")
            return
        return func(*args, **kwargs)
    return wrapper


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli():
    """A Python-based Command-Line Interface (CLI) application for managing workshop bookings and one-on-one meetings."""
    pass

@cli.command()
@click.option('--email', '-e', prompt='Please enter your email', required=True, help='Email of a registered user.')
@click.option('--password', '-p', prompt='Please enter your password', required=True, help='Password of a registered user.')
def login(email, password):
    """Log in to the application."""
    # sign_in()
    # Simulate successful login
    if email == "sakhi@example.com" and password == "kode":
        session['user'] = email 
        click.echo("Login successful!")
    else:
        click.echo("Invalid email or password. Please try again.")

@cli.command()
def logout():
    """Log out of your account."""
    if 'user' in session:
        session.pop('user')
        click.echo("Logged out successfully.")
    else:
        click.echo("You are not logged in.")

@cli.command()
@click.option('--email', '-e', prompt='Please enter your email', required=True, help='New user email.')
@click.option('--password', '-p', prompt='Please enter your password', required=True, help='New user password.')
def sign_up(email, password):
    """Add new user to application."""
    sign_up()


def view_workshops():
    """List upcoming workshops and mentors available for booking."""
    ...
def request_meeting():
    """Request a mentor or peer session."""
    ...
def view_bookings():
    """Display a list of all confirmed bookings."""
    ...
def cancel_booking():
    """Allow users to cancel an existing booking."""
    ...


if __name__ == '__main__':
    cli()
