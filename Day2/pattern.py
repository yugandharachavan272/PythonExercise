# Write a Python program to print Pascal triangle up to n rows.
rowsForPascalTri = int(input("Enter no of rows for Pascal triangle : "))


fil = '*'
for i in range(1, rowsForPascalTri + 1):
    # for j in range(1, (rowsForPascalTri + 1) - i):
    # print rowsForPascalTri - i
    print ' ' * (rowsForPascalTri - i),
    print fil * i
    # print ""

fill = '*'
# print fill.center(5)
for i in range(1, rowsForPascalTri + 1):
    print (fill * i)

fill = '#'
rows = range(1, rowsForPascalTri + 1)
for i in rows[::-1]:
    print fill * i

fill = "*"
count = rowsForPascalTri - 1
for i in range(1, rowsForPascalTri + 1):
    for j in range(1, count + 1):
        print " ",
    count -= 1
    listofstart = range(1, i+1, 1)  # range(1, i + (i - 1) + 1)
    for k in listofstart:
        print fill,
    print ""

fill = "*"
count = rowsForPascalTri - 1
for i in range(1, rowsForPascalTri + 1):
    listofstart = range(1, i+1, 1)  # range(1, i + (i - 1) + 1)
    for k in listofstart:
        print fill,
    count -= 1
    for j in range(1, count + 1):
        print " ",
    print ""

fill = "*"
count = rowsForPascalTri - 1
for i in range(1, rowsForPascalTri + 1):
    for j in range(1, count + 1):
        print " ",
    count -= 1
    listofstart = range(1, i * 2, 1)  # 2 * i -1  //  i + (i - 1) + 1
    for k in listofstart:
        print fill,
    print ""



def binomialCoeff(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res


rows = int(rowsForPascalTri)
count = rowsForPascalTri - 1
for line in range(0, rows):
    # Every line has number of
    # integers equal to line
    # number
    for j in range(1, count + 1):
        print " ",
    count -= 1
    for i in range(0, line + 1):
        print binomialCoeff(line, i),
        print " ",
    print ""


