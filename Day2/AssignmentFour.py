# Write a Python program to enter a number and print its reverse.
digit_number = input("Enter a number")
numberList = map(int, str(digit_number))
print "List: ", numberList
rnumberList = numberList[::-1]
print "Reverse List: ", rnumberList
reverseNumber = "".join(map(str, rnumberList))
print "Reverse of {} is {}".format(digit_number, reverseNumber)
# Write a Python program to check whether a number is palindrome or not.
if int(digit_number) == int(reverseNumber):
    print "Entered number is palindrome"
else:
    print "Entered number is not palindrome"

# Write a Python program to find frequency of each digit in a given integer.
countOfDigitsInNumber = {}
distNumberList = list(set(numberList))
# print distNumberList
for i in distNumberList:
    print " Number {}, Count {}".format(i, numberList.count(i))
    countOfDigitsInNumber[i] = numberList.count(i)
    # print countOfDigitsInNumber

# Write a Python program to find power of a each number using for loop
print "Digits in number are ", distNumberList
exponent = int(input("Please Enter Exponent Value : "))
for i in distNumberList:
    print "{} power {} is {}".format(i, exponent, i ** exponent)

# Write a Python program to print all ASCII character with their values
# ASCII defines 128 characters whose byte values range from 0 to 127 inclusive
print ''.join([chr(i) for i in range(128)])

for i in range(128):
    print "ASCII VALUE FOR {} is {}".format(chr(i), i)

