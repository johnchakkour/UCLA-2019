a = int(input())
fac = 1
i = 1

while i <= a:
   fac = fac * i
   i = i + 1
print(fac)

a = int(input())
f0 = 0
f1 = 1
next_val = (f0+f1)**4
i = 0
while i<=a:
    next_val = (f0+f1)**4
    f0 = f1
    f1 = next_val
    i = i+1
print(next_val)