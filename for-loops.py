import random
import math

#print(a)
#sum = 0
#for x in a:
#    sum = sum + x
#print(sum)

def isPrime(n):
    for x in range(2,n):
        if n%x == 0:
            return False
    return True
n = int(input())
print(isPrime(n))

