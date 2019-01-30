
number = 10
name = 'Yugandhara'
location = 'Pune'
number1 = number2 = number3 = 1
print number1, number2, number3

# Multiple assignment
number1, number2 = 10, 20

print number
print name
print location
print number1, number2, number3

number_int = 10
print number_int, type(number_int)
number_int = 2147483647
print number_int, type(number_int)
number_int = 2147483648
print number_int, type(number_int)
number_comp = 3 + 4j
print number_comp, type(number_comp)
number_float = 3.7
print number_float, type(number_float)

# Built in functions
number = -10
number1 = abs(-10)
print 'number', number
print 'number1', number1

number = -10.1
numberComp = 3 + 4j
print 'abs of %d is %d' % (number, abs(number))
print 'abs of %d is %f' % (number, abs(number))
print 'abs of %s is %s' % (number, abs(numberComp))
print abs(numberComp)
'''
# Number functions
number = int('1010', 2)
print 'int', number
print 'float', float(10)
print 'long', long(12)
print 'complex', complex(1, 2)
'''

#  cmp: Return negative if x<y, zero if x==y, positive if x>y.

print 'cmpRes1', cmp(3, 2)
print 'cmpRes2', cmp(1, 2)
print 'cmpRes3', cmp(2, 2)

# isinstance
print 'isinstance Result 1: ', isinstance(1, int)
print 'isinstance Result 2: ', isinstance(1.1, float)
print 'isinstance Result 3: ', isinstance(1L, long)
print 'isinstance Result 4: ', isinstance(complex(1, 2), complex)

# numbers operation
print 10+2
print 10 - 2
print 10 * 2
print 10 ** 2
print 11 % 2
print 10 * 2 ** 2
print 10 * 2 / 5 % 1 + 3 - 5

print bin(10)
print bin(-10)

# String Formatting, slicing
name = 'yugandhara'
print type(name)
print len(name)
print isinstance('uga', str)
print isinstance(10, str)
print isinstance(str(10), str)
print chr(65)
print name[4]  # string indexing
print 'reverse string', name[::-1]
print 'name 1', name[::2]   # string slicing
print 'name 2', name[:-11:-1]  # string slicing
print 'name 2', name[-5:-11:-1]  # string slicing
print 'we are at %s turning %d' % ('YUga', 20)   # string formatting
print 'we turning at  %d today' % 20

# List
names = ['yuga', 'Yuvi', 'Pravin', 'Kavya']
print names[0]  # first
print names[-1]  # first from Last
print names[-2]  # second from Last
print type(names)
print 'length of names is:', len(names)
print 'any in names:', any(names)
print 'all in names:', all(names)
print names + names  # arithmetic on list
print 'multiplication', names * 3
# List slicing and formating
print names[0:2]
print names[::-1]
print 'eg', names[1::]

# Range
print range(10)
print range(1, 10)
print range(1, 10, 2)  # Odd
print range(2, 16, 2)  # Even

# list of list
names = [['yuga', 25], ['pravin', 28]]
print 'names are : ', names[0][0], names[1][0]
names[0] = 'YUGA'

print names

# tuple
names = ('yuga', 'Pravin', 'Chougale')
print type(names)
names = ('yuga')
print type(names)
names = ('yuga',)
print type(names)
print names

# list is fixed and mutable we can  assign names[0] = 'YUGA'
# tuples are immutable we can not assign names[0] = 'YUGA'


# Dictionary
Employee = {'name': 'yuga', 'Id': 1, 'Age': 25}
print Employee
print Employee['name']
print Employee.items()
print Employee.keys()
Employee['Location'] = 'Pune'
print Employee

# SET

managers = set(['kavya', 'neha','neha', 'nitin'])
print type(managers)
print managers  # re4turns only unique values

# identity operators
# if numbers values same then same identity
# if string values same but different varibles then different identiy because it has different memory allocation
# is and is not is used
# Quiz
print sum([1, 2, 3, 4, 5])
name = 'Ethans Technologies'
print name[0:6]
print name[-1:0]











