name = input("What's your name? ")
print (name + "'s list")
d = {}

add = input("Do you want to add something to your grocery list? Type yes or no. ")
if add == "yes":
    key = input("What do you want to add? ")
    d[key] = 1
for key in d:
    print (key, 'has a quantity of', d[key])
    

test = True
while test == True:
    answer = input("What do you want to do? Type either add, update, delete, print or done. ")
    if answer == "add":
        insert = input("What do you want to add? ")
        d[insert] = 1
    elif answer == "update":
        update = input("What do you want to update? ")
        if update not in d:
            print("You are adding a new item to the list. This item doesn't currently exist.")
            d[update] = 1
        value = input("How many of that item do you want? ")
        d[update] = value
    elif answer == "delete":
        delete = input("What do you wish to remove? ")
        if delete not in d:
            print("Error. Item doesn't exist.")
        d.pop(delete, None)
    elif answer == "print":
        for key in d:
            print (key, 'has a quantity of', d[key])
    elif answer == "done":
        test = False
    else:
        print("Error. Please type the correct option.")
    
