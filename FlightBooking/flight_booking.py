from passenger import Passenger
from flight_details import BookingClass, SeatingArea, Flight


# Example usage
def main():
    print("\n\nWelcome! To Booking System...!!!\n")
    restart = 'Y'
    while restart != ('N', 'NO', 'n', 'no'):
        total_rows = input("Enter total rows count ")
        business_rows = int(input("Enter rows in business class : "))
        economy_rows = int(input("Enter rows in economy class : "))

        if int(business_rows) + int(economy_rows) == int(total_rows):
            print ("******** Please enter no of seats per row maximum 5 and minimum 2  ********")
            business_seats = int(input("Enter no of seats in row for business class : "))
            economy_seats = int(input("Enter no of seats in row for economy class : "))
            # business = SeatingArea(BookingClass.BUSINESS, start_row=1, row_count=5, seats_per_row=4)
            # economy = SeatingArea(BookingClass.ECONOMY, start_row=6, row_count=20, seats_per_row=6)
            business = SeatingArea(BookingClass.BUSINESS, start_row=1, row_count=business_rows,
                                   seats_per_row=business_seats)

            economy = SeatingArea(BookingClass.ECONOMY, start_row=(business_rows + 1), row_count=economy_rows,
                                  seats_per_row=economy_seats)

            flight = Flight(economy, business)
            flight.print_statistics()

            print("*************** GO TO BOOK FLIGHT *******************")

            book_ticket = 'Y'
            while book_ticket != ('N', 'NO', 'n', 'no'):
                ask_window = raw_input("Are you looking for window seat..?")
                is_window = 0
                if ask_window in ('y', 'YES', 'yes', 'Yes', '1', 1):
                    is_window = 1
                passenger_name = raw_input("Enter Passenger name : ")
                john = Passenger(passenger_name)
                print("1. Business Class ")
                print("2. Economy Class ")
                flight_class = int(raw_input("Enter Passenger name : "))

                is_booking_done = False  # type: bool
                if flight_class == 1:
                    is_booking_done = john.book(flight, BookingClass.BUSINESS, is_window)
                else:
                    is_booking_done = john.book(flight, BookingClass.ECONOMY, is_window)

                # john.book(flight, BookingClass.ECONOMY, is_window)
                # print(john.seat)
                # print(john.booking_id)
                # flight.print_statistics()

                if is_booking_done:
                    print ("{}, your booking done successfully...!!".format(passenger_name))
                    print("YOur seat no is {} and booking id is {} ".format(john.seat, john.booking_id))

                    flight.print_statistics()

                    book_ticket = raw_input("Do you want to book another seat ?")
                    if book_ticket in ('y', 'YES', 'yes', 'Yes', '1', 1):
                        book_ticket = 'Y'
                    else:
                        print (" Thank you to visit our system...!!!")
                        exit(0)

                else:
                    print ("Sorry we cant book your ticket.. check the following result ")
                    flight.print_statistics()

                    book_ticket = raw_input("Do you want to retry ?")
                    if book_ticket in ('y', 'YES', 'yes', 'Yes'):
                        book_ticket = 'Y'
                    else:
                        print (" Thank you to visit our system...!!!")
                        exit(0)
            else:
                print (" Thank you to visit our system...!!!")
                exit(0)
        else:
            print ("Sorry...!!! Classes rows count doesnt match with total rows..")
            restart = raw_input("Do you want to restart ?")
            if restart in ('y', 'YES', 'yes', 'Yes'):
                restart = 'Y'
            else:
                print (" Thank you to visit our system...!!!")
                exit(0)


if __name__ == '__main__':
    main()
