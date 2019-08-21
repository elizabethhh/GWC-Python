import random
fiveSyllables= ["The softest whisper", "The breezy wind  blows", "The gentle purring", "Sally sells seashells", "Between the two trees", "A cat and a dog", "An airplane buzzes by", "Peaceful and quiet", "What is happening", "On the shoreside here"]
lengthFive= len(fiveSyllables) - 1
indexFive1= random.randint(0, lengthFive)
indexFive2= random.randint(0, lengthFive)

sevenSyllables= ["How quiet the lake is now", "When the bird flies by above", "The colorful notes lie there", "Through the dark and dim forest", "As the sun shines brightly now", "The rose blooms in the garden", "Colorful cool animals", "Fancy cats dance everywhere", "Singing and dancing today", "A card drops from her backpack"]
lengthSeven= len(sevenSyllables) -1
indexSeven= random.randint(0, lengthSeven)

for i in range(3):
    print (fiveSyllables[indexFive1] + "\n" + sevenSyllables[indexSeven] + "\n" + fiveSyllables[indexFive2])
    print (" ")
    indexFive1= random.randint(0, lengthFive)
    indexFive2= random.randint(0, lengthFive)
    indexSeven= random.randint(0, lengthSeven)

poemName = input("What would you like to name your poem? ")
print("Nice name! \nThe poem's name is: " + poemName)
