def replaceNegatives(a2DList):
    for x in range(len(a2DList)):
        for y in range(len(a2DList[x])):
            if a2DList[x][y] < 0:
                a2DList[x][y] = "Nope"
    print(a2DList)

x = [[4,2,-3,87],[-34,5]]
print(x)
print(replaceNegatives(x))


a = [3,-6,10]
for i in range(len(a)):
    if a[i] < 0:
        a[i] = "None"
print(a)
