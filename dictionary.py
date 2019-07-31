dictionary = {
    "mint":"clean",
    "lit":"cool",
    "chuffed":"pleased"
}
print(dictionary.values())

print(dictionary["mint"])
print(dictionary["lit"])
print(dictionary["chuffed"])

sentence = "This party's lit I'm pretty chuffed with my mint clothes"
wordList = sentence.split(" ")
print(wordList) 

for word in wordList:
    if word in dictionary.keys():
        print(dictionary[word]) 
