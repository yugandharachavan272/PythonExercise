# Write a Python program to find sum of all natural numbers between 1 to n
number = input("Enter number ")
natural_numbers = range(1, int(number) + 1)
count = 0
Result = 0
for i in natural_numbers:
    if count < int(number):
        Result += int(number)
        count += 1
else:
    print " sum of natural numbers from 1 to %s is %d" % (number, Result)

# Write a Python program to find sum of all even numbers between 1 to n
# number = input("Enter number ")
natural_numbers = range(2, int(number) + 1, 2)
Sum = sum(natural_numbers)
print "sum of all even numbers between 1 to %s is %d " %(number, Sum)


# Write a Python program to find sum of all odd numbers between 1 to n.

natural_numbers = range(1, int(number) + 1,2)
Sum = sum(natural_numbers)
print "sum of all odd numbers between 1 to %s is %d " % (number, Sum)

# Write a Python program to count number of digits in a number.

digit_number = input(" Enter a number to count digit: ")
count = 0
while digit_number > 0:
    count += 1
    # Divides and returns the integer value of the quotient. It dumps the digits after the decimal. Floor division
    digit_number = digit_number // 10
print "The number of digits in the number are:", count





