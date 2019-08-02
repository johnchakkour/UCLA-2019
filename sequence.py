import math

#first sequence submitted
f0 = 0
f1 = 1
next_val = (f0+f1)**4
i = 0
while i <= 5:
    next_val = (f0+f1)**4
    f0 = f1
    f1 = next_val
    i = i+1
    print(next_val)

#second sequence submitted
for x in range(100):
    print((x**2)-(x**3)+(x**4))