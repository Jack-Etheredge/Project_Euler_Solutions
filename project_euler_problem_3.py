# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

checknum=600851475143
i=1

while checknum>1:
    i+=1
    while checknum%i==0:
        checknum=checknum/i
        largest=i

print(largest)
