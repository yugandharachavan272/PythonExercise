import random


class Passenger:
    def __init__(self, name):
        self.name = name
        self.booking_id = None
        self.seat = None

    def has_booked(self):
        return self.booking_id is not None

    def book(self, flight, booking_class, is_window):
        if is_window == 0:
            if flight.remaining_seat_count(booking_class) != 0:
                self.seat = flight.get_seat(booking_class)
                self.booking_id = random.Random().randrange(1000, 10000)
                return True
        else:
            if flight.remaining_window_seat_count(booking_class) != 0:
                self.seat = flight.get_window_seat(booking_class)
                self.booking_id = random.Random().randrange(1000, 10000)
                return True

        return False

