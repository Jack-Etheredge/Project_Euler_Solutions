# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

primes=[2,3,5,7]
for i in range(7,2000000)[::2]:
	checkprime=True
	for prime in primes:
		if i%prime==0:
			checkprime=False
			break
	if checkprime==True:
		primes.append(i)
# print(i,\"/2000000\")
print(sum(primes))

# adding the break and skipping even numbers speeds up the code substantially
# this needs to be made much more efficient still, however