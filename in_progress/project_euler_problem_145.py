# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).
# 
# There are 120 reversible numbers below one-thousand.
# 
# How many reversible numbers are there below one-billion (109)?

maxnum = 10**9
countnums = 0

for i in range(10, maxnum+1):
    checkodddigits = True
    if int(str(i)[-1]) == 0:
        checkodddigits = False
    sumnum = i+int(str(i)[::-1])
    for j in range(len(str(sumnum))):
        if int(str(sumnum)[j]) % 2 == 0:
            checkodddigits = False
    if checkodddigits == True:
        countnums += 1
    if i%100==0:
        print(round((i/maxnum)*100,2),"%")

print(countnums)

# This code is SUPER inefficient. It takes a very long time to run (2h21m).
# We could save a bit of computation by excluding numbers that start and end in an even number, because then we know the sum will have an even digit.