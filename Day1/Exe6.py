# number is inside string
x = "There are %d types of people." % 10
# simple assignment of string to variable binary
binary = "binary"
# simple assignment of string to variable do_not
do_not = "don't"
# here substitution of string inside string
# Eg of string inside string
y = "Those who know %s and those who %s." % (binary, do_not)

# print variable x value
print x
# print variable y value
print y
# here substitution of un formatted string inside string of
# Eg of string inside string
print "I said: %r." % x
# here substitution of formatted string inside string of
# Eg of string inside string
print "I also said: '%s'." % y

# assignment of boolean value to variable
hilarious = False
# assignment of string
joke_evaluation = "Isn't that joke so funny?! %r"

# first print joke_evaluation variable value and hilarious variable for substitution of %r i.e. un formatted string
# Eg of string inside string
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# concatenation of two strings
print w + e
