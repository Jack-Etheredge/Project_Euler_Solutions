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
