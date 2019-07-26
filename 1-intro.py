starWarsList = ["Star Wars","star wars","Star wars","star Wars"]
originalTrilogyList = ['A New Hope','a new hope','ANH','anh','Empire Strikes Back',
'empire strikes back','ESB','esb','Return of the Jedi','return of the jedi','ROTJ','rotj']
name = input("What is your name? ")
if name == 'John' or name == 'john':
    print("Nice to meet you,",name)
else:
    print("That's an alright name. Not as nice as John though.")
age = input("How old are you? ")
if age < '28':
    print("How young. Oh to be", age, "again! I was created in 1991, so that makes me 28.")
else:
    print("Oh finally! I've only been meeting teenagers lately. It's great to see someone more... experienced.")
home = input("Where do you live? ")
print("Nice! I've been to", home)
print("Well technically, I've been to every country in the world.")
movie = input("What's your favorite movie? ")
if movie in starWarsList:
    print("Me too!")
    favSWmovie = input("Which film do you like best? ")
    if favSWmovie in originalTrilogyList:
        print('I agree. The whole Original Trilogy is great')
    elif favSWmovie == 'rogue one' or 'Rogue One':
        print("That's a great movie.")
    else:
        print('I disagree. Any film from the Sequel Trilogy is garbage.')
else:
    print("Great film. Not my favorite though.")

x = int(input("Type a number. I will check if it is even or odd. "))
if (x % 2 == 0):
    print(x,"is even")
else:
    print(x,"is odd")
