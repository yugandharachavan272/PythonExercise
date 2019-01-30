# Write a Python program to print all natural numbers from 1 to n.
number = input("Enter number ")
natural_numbers = range(1, int(number) + 1)
count = 0
for i in natural_numbers:
    if count == 0:
        print "natural numbers are as follows: \n"
    if count < int(number):
        print i,
        count += 1

# Write a Python program to print all natural numbers in reverse (from n to 1).
Reverse_numbers = natural_numbers[::-1]
# print Reverse_numbers
count = 0
for i in Reverse_numbers:
    if count < int(number):
        if count == 0:
            print "natural numbers in reverse are as follows: \n"
        print i,
        count += 1


# Write a Python program to print all alphabets from a to z.
small_letters = map(chr, range(ord('a'), ord('z')+1))
print "\n"
for i in small_letters:
    print i,

#  Write a Python program to print all odd numbers between 1 to 100
print "\n all odd numbers between 1 to 100: "
for i in range(1, 100, 2):
    print i,

#  Write a Python program to print all even numbers between 1 to 100
print "\n all even numbers between 1 to 100: "
for i in range(2, 101, 2):
    print i,
