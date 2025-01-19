import datetime

from termcolor import cprint


class BookingSystem:
    def __init__(self):
        """Initialize available slots (1-hour slots)"""
        self.available_slots = self.generate_slots()
        self.bookings = {}

    def generate_slots(self):
        """Generate available time slots for today."""
        now = datetime.datetime.now()
        today = now.date()
        slots = []
        for hour in range(9, 17): # 09:00 to 17:00
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
                cprint(f"Slot booked successfully for {user_name} at {slot.strftime('%Y-%m-%d %H:%M')}.", "green")
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
            