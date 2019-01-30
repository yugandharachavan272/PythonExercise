
# Write a Python program to find first and last digit of a number.
digit_number = input(" Enter a number to find first and last digit of a number: ")
digits = map(int, str(digit_number))
print type(digits)
print digits
print "First digit of number is ", digits[0], " and last is", digits[len(digits)-1]
#  Write a Python program to find sum of first and last digit of a number.
print " Sum of {} and {} is {}".format(digits[0], digits[len(digits)-1], (digits[0] + digits[len(digits)-1]))
# Write a Python program to swap first and last digits of a number.
first = digits[0]
last = digits[len(digits)-1]
digits[0] = last
digits[len(digits)-1] = first
result = int("".join(map(str, digits)))
print " Digits after swapping:", digits
print "After swapping first and last digit of {} is {}".format(digit_number, result)
# Write a Python program to calculate sum of digits of a number.
sumOfDigits = sum(digits)
print "sum of all digits in {} is {}".format(digit_number, sumOfDigits)
# Write a Python program to calculate product of digits of a number
mulOfDigits = reduce((lambda x, y: x * y), digits)
sumOO = map((lambda x, y: x + y), digits, digits)
print "sumOO ", sumOO
print "Multiplication of all digits in {} is {}".format(digit_number, mulOfDigits)