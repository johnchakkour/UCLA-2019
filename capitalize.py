#s = "josePH JiMmy john jAmes jASMine"
#wordList = s.split()
#print(wordList)

#for x in wordList:
#    x = x.capitalize()
#    print(x)

#for x in range(101):
#    if x%3 == 0 and x%5 == 0:
#        print("fizz buzz")
#    elif x%3 == 0:
#        print("fizz")
#    elif x%5 == 0:
#        print("buzz")
#    else:
#        print(x)
 

changeAmount = int(input("How much changeAmount do you need?\n"))
quarters = 0
dimes = 0
nickels = 0
pennies = 0

quarters = int(changeAmount/25)
changeAmount = changeAmount%25
dimes = int(changeAmount/10)
changeAmount = changeAmount%10
nickels = int(changeAmount/5)
changeAmount = changeAmount%5
pennies = int(changeAmount/1)
changeAmount = changeAmount%1


print(quarters,"quarters,",dimes,"dimes,",nickels,"nickels,",pennies,"pennies")