# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

primenum = 10001
i=0
testnum=2

while i < primenum:
	checkprime = True
	for j in range(2,testnum):
		if testnum%j==0:
			checkprime=False
	if checkprime==True:
		i+=1
		currentprime=testnum
		# print("prime number",i,"is",currentprime)
	testnum+=1

print(currentprime)

# This code takes a while to run (10m4s)
# We could speed it up by doing things like skipping numbers divisible by 2 and 3 from checking

primenum = 10001
i=1 # we're skipping evens, so we now need to add 1 to our count for 2
testnum=3

while i < primenum:
	checkprime = True
	for j in range(3,testnum):
		if testnum%j==0:
			checkprime=False
	if checkprime==True:
		i+=1
		currentprime=testnum
		# print("prime number",i,"is",currentprime)
	testnum+=2	

print(currentprime)

# This code is faster (twice as fast @ 5m6s), but there's still room for improvement:

primenum = 10001
i=3 # including 2,3,5 that we skip
testnum=7

while i < primenum:
	checkprime = True
	for j in range(7,testnum):
		if testnum%j==0:
			checkprime=False
	if checkprime==True:
		i+=1
		currentprime=testnum
		# print("prime number",i,"is",currentprime)
	testnum+=2	
	if testnum%3==0:
		testnum+=2
	if testnum%5==0:
		testnum+=2
		
print(currentprime)

# We're now down to 3m3s, which is over 3 times as fast as the original code
# There are more complicated math tricks involving prime numbers, but this speeds up the code a lot without going crazy.

