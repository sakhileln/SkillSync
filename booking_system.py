"""
A simple booking system that allows users to view available 1-hour time slots, 
book slots, and view their current bookings. Time slots are generated for the 
current day between 09:00 and 17:00. The system prevents double-booking and 
provides a user-friendly terminal interface.
"""

import datetime

from termcolor import cprint


class BookingSystem:
    """Simple booking system class."""

    def __init__(self):
        """Initialize available slots (1-hour slots)"""
        self.available_slots = self.generate_slots()
        self.bookings = {}

    def generate_slots(self):
        """Generate available time slots for today."""
        now = datetime.datetime.now()
        today = now.date()
        slots = []
        for hour in range(9, 17):  # 09:00 to 17:00
            slot_time = datetime.datetime.combine(today, datetime.time(hour))
            slots.append(slot_time)
        return slots

    def display_available_slots(self):
        """Display available slots."""
        print("Available Slots:")
        for i, slot in enumerate(self.available_slots):
            cprint(f"{i + 1}: {slot.strftime('%Y-%m-%d %H:%M')}", "yellow")

    def book_slot(self, slot_number, user_name):
        """Book a slot."""
        if 0 < slot_number <= len(self.available_slots):
            slot = self.available_slots[slot_number - 1]
            if slot not in self.bookings:
                self.bookings[slot] = user_name
                # pylint: disable=line-too-long
                cprint(
                    f"Slot booked successfully for {user_name} at {slot.strftime('%Y-%m-%d %H:%M')}.",
                    "green",
                )
                # Remove the booked slot from available slots
                self.available_slots.remove(slot)
            else:
                cprint("This slot is already booked.", "red")
        else:
            cprint("Invalid slot number.", "red")

    def view_bookings(self):
        """View all bookings."""
        if not self.bookings:
            cprint("No bookings found", "red")
            return
        cprint("Current Bookings.", "green")
        for slot, user in self.bookings.items():
            cprint(f"{user} has booked {slot.strftime('%Y-%m-%d %H:%M')}.", "green")


def bookings():
    """Main driver program to test BookingSystem class."""
    system = BookingSystem()

    while True:
        cprint("\n--- Booking System ---", "blue")
        cprint("1. View Available Slots", "blue")
        cprint("2. Book a Slot", "blue")
        cprint("3. View My Bookings", "blue")
        cprint("4. Exit", "blue")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.display_available_slots()
        elif choice == "2":
            system.display_available_slots()
            try:
                slot_number = int(input("Enter the slot number to book: "))
                user_name = input("Enter your name: ")
                system.book_slot(slot_number, user_name)
            except ValueError:
                cprint("Please enter a valid number.", "red")

        elif choice == "3":
            system.view_bookings()

        elif choice == "4":
            cprint("Exiting the booking.", "green")
            break
        else:
            cprint("Invalid choice. Please try again.", "red")


if __name__ == "__main__":
    # Test booking system.
    bookings()
