import random
adjectiveMenu= ["Spicy", "Sweet", "Delicious", "Sour", "Cold", "Special", "Bitter", "Vegan", "Salty", "Flavorful"]
cookingStyleMenu= ["grilled", "American", "Italian", "Chinese", "baked", "Indian", "Mexican", "Jamaican", "boiled", "Filipino"]
foodMenu= ["dumplings", "pasta", "soup", "sushi", "pizza", "burger", "chicken", "fish", "rice", "beans"]

adjective_length = len(adjectiveMenu) -1
cooking_length = len(cookingStyleMenu) -1
food_length = len(foodMenu) -1

adjective_random_index = random.randint(0, adjective_length)
cooking_random_index = random.randint(0, cooking_length)
food_random_index = random.randint(0, food_length)

def printItem(number):
    print(str(number) + ". " + adjectiveMenu[adjective_random_index] + " " + cookingStyleMenu[cooking_random_index] + " " + foodMenu[food_random_index])

number= 1
for i in range (10):
    printItem(number)
    adjective_random_index = random.randint(0, adjective_length)
    cooking_random_index = random.randint(0, cooking_length)
    food_random_index = random.randint(0, food_length)
    number += 1
    
