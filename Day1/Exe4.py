# no of cars
cars = 100
# space in car
space_in_a_car = 4.0
# drivers
drivers = 30
# passengers
passengers = 90
# cars not driven
cars_not_driven = cars - drivers
# cars driven
cars_driven = drivers
# carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# average passengers per car
average_passengers_per_car = passengers / cars_driven

# Here = is for assignment
# here _ is imaginary space

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."


# Extra credit
# 1. space_in_a_car is floating point number for accurate result numeric operations with int gives float \
# so to get accurate carpool_capacity we use 4.0


x = 1.5
y = 5

i = x + y
print i
print "number", int(i)
