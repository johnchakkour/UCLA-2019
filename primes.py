import random
import math

def isPrime(n):
    for x in range(2,n):
        if n%x == 0:
            return False
    return True
n = int(input())
print(isPrime(n))

