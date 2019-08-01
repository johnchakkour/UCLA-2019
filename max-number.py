def max(a,b):
    if a>b:
        return a
    else:
        return b

a = input()
b = input()
print(max(a,b), "is bigger")

import math

def findMax(a):
    b = a[0]
    for x in a:
        if x > b:
            b = x
    return b

a = ['daisy','Daisy','twenty','why','Twenty']
print(findMax(a))