# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

def findmultiplessum (lower, upper):
	sumval=0
	for i in range (lower, upper):
		if i%3==0 or i%5==0:
			sumval+=i
	return(sumval)
	print(sumval)
		
lower = 1
upper = 1000
	
sumval=findmultiplessum(lower,upper)
print(sumval)
