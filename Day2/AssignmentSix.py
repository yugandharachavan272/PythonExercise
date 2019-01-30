# Write a Python program to check whether a number is Armstrong number or not
number = raw_input("Enter number to check Armstrong: ")
lengthOfNumber = len(number)
numberList = map(int, str(number))
sumOfExponentOfDigits = sum(list(i**lengthOfNumber for i in numberList))
# print sumOfExponentOfDigits
if int(number) == sumOfExponentOfDigits:
    print number, "is Armstrong number"
else:
    print number, "is not Armstrong number"

# Write a Python program to print all Armstrong numbers between 1 to n.
rangeOfArmstrong = input("Enter range to find armstrong number")
print "*** Armstrong between 1 to {} is as follows:".format(rangeOfArmstrong)
for i in range(1, rangeOfArmstrong + 1):
    lengthOfNumber = len(str(i))
    numberList = map(int, str(i))
    sumOfExponentOfDigits = sum(list(i ** lengthOfNumber for i in numberList))
    # print "num:", i, " sum", sumOfExponentOfDigits
    if int(i) == sumOfExponentOfDigits:
        print i, ",",

# Write a Python program to print Fibonacci series up to n terms.
rangeOfFib = input("\nEnter range to get fibonacci series : ")
print range(1, int(rangeOfFib) + 1)
for i in range(1, int(rangeOfFib) + 1):
    num = i
    fib1 = 0
    fib2 = 1
    count = 2
    series = (fib1, fib2)
    while count < num:
        fib3 = fib1 + fib2
        series += (fib3,)
        fib1 = fib2
        fib2 = fib3
        count += 1
    else:
        print "Fib of {} is {}".format(num, series)

