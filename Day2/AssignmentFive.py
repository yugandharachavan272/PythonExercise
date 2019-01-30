# Write a Python program to calculate factorial of a number
number = input("Enter Number")
fact = 1
for i in range(1, int(number) + 1):
    fact *= i
print "*** Factorial of {} is {}".format(number, fact)

# Write a Python program to check whether a number is Prime number or not
count = 0
for i in range(2, int(number)):
    count += 1
    if number % i == 0:
        print "*** Number is not prime ***"
        break
    elif count == len(range(2, int(number))):
        print "*** Number is prime ***"

# Write a Python program to find HCF (GCD) of two numbers.
# Write a Python program to find LCM of two numbers.
print "Enter numbers to find HCM and LCM..."
first_number = int(input("First : "))
second_number = int(input("second : "))


def gcd(a, b):
    # Everything divides 0
    if a == 0:
        return b
    if b == 0:
        return a

        # base case
    if a == b:
        return a

        # a is greater
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


# Driver program to test above function
a = first_number
b = second_number
HCF = gcd(a, b)
if HCF:
    print('GCD(HCF) of', a, 'and', b, 'is', HCF)
    print('LCM of', a, 'and', b, 'is', (a*b) / HCF)
else:
    print('not found')

# Write a Python program to print all Prime numbers between 1 to n.
rangeOfPrimeNumber = input("Enter range to find prime numbers: ")
print "Prime numbers between a and ", rangeOfPrimeNumber, " is as follows : "
for i in range(1, 3):
    print i, ",",
for i in range(2, int(rangeOfPrimeNumber) + 1):
    isNotPrime = 0
    countOfNumbers = 0
    # print "i", i
    for j in range(2, int(i)):
        countOfNumbers += 1
        # print "i:", i, " j:", j
        if int(i) % int(j) == 0:
            isNotPrime = 1

        # print "isNotPrime: ", isNotPrime
        # print "countOfNumbers: ", countOfNumbers, "len:", len(range(2, int(i)))
        if countOfNumbers == len(range(2, int(i))):
            # print " isNotPrime ", isNotPrime
            if isNotPrime == 0:
                # print "{} is Prime number".format(i)
                print i, ",",

