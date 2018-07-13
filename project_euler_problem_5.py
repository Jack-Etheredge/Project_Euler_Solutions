# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

lower = 1
upper = 20
smallestnum = upper # we know this is the smallest it could possibly be
checknum=False
while checknum==False:
    checknum=True
    smallestnum+=1
    for i in range(lower,upper+1):
        if smallestnum%i!=0:
            checknum=False
print(smallestnum)

# This took 9.5 minutes to run, so I strongly suspect there's a more clever solution.