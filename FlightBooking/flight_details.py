letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class BookingClass:
    ECONOMY = 'Economy'
    BUSINESS = 'Business'


class Seat:
    def __init__(self, row_number, letter):
        self.row_number = row_number
        self.letter = letter

    def __str__(self):
        return '{}{}'.format(self.row_number, self.letter)


class SeatingArea:
    def __init__(self, booking_class, start_row, row_count, seats_per_row):
        self.booking_class = booking_class
        self.seat_count = row_count * seats_per_row
        self.seats_remaining = []
        self.seats_windows_remaining = []
        # print(" seats_windows_remaining ", len(self.seats_windows_remaining))
        # print " i m in seating area "
        for row_number in range(start_row, row_count + start_row):
            # print "booking_class ", booking_class, " range(seats_per_row) ", range(seats_per_row)
            for seat_number in range(seats_per_row):
                new_seat = Seat(row_number, letters[seat_number - 1])
                if seat_number == 0:
                    self.seats_windows_remaining.append(new_seat)
                elif seat_number == (seats_per_row - 1):
                    self.seats_windows_remaining.append(new_seat)
                else:
                    self.seats_remaining.append(new_seat)

        # print(" seats_windows_remaining ", len(self.seats_windows_remaining))
        # print(" seats_remaining ", len(self.seats_remaining))


class Flight:
    def __init__(self, economy_seats, business_seats):
        # should I use the SeatingArea.booking_class attribute as the key?
        self.seating_areas = {
            BookingClass.ECONOMY: economy_seats,
            BookingClass.BUSINESS: business_seats}

    def print_statistics(self):
        for booking_class, seating_area in self.seating_areas.items():
            print ('In {} class we have window seats : {} , others: {} '.
                   format(booking_class, len(seating_area.seats_windows_remaining), len(seating_area.seats_remaining)))
            # print('{}: {}% available'.format(
            #     booking_class,
            #     len(seating_area.seats_remaining) / seating_area.seat_count * 100))

    def remaining_seat_count(self, booking_class):
        return len(self.seating_areas[booking_class].seats_remaining)

    def remaining_window_seat_count(self, booking_class):
        return len(self.seating_areas[booking_class].seats_windows_remaining)

    def get_seat(self, booking_class):
        return self.seating_areas[booking_class].seats_remaining.pop()

    def get_window_seat(self, booking_class):
        return self.seating_areas[booking_class].seats_windows_remaining.pop()
