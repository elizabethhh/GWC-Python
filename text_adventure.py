start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze. A sign is hanging from the ivy: "You have one hour.
Don't touch the walls." There is a hallway to your right and to your left.
'''
print(start)
user_input = input("Type 'left' to go left or 'right' to go right. ")
win = '''
You open the door and you are out! You have escaped the dreadful maze.
All of a sudden your alarm clock rings and you are forced to wake up
and start your day. It was all a dream after all.
GAME OVER.
'''
gameOver = '''
You didn't escape the maze. The hour is up!
Just in time, your alarm clock rings and you are forced
to wake up and start your day. It was all a dream after all.
GAME OVER.
'''
noTime= "You avoid the door and keep walking. Eventually, time runs out."
                                    
#START GAME
if user_input == "left":
    leftTurn = '''
    You decide to go left and you take many confusing turns in the maze while staying
    careful to avoid the walls. You're exhausted, dehydrated, and hungry.
    It feels like there's no hope left. Suddenly, you see three paths in front of you.
    You decide to take the middle path; however, as you continue walking, you hear
    a faint growling noise. You finally see the source of the noise. 
    It's snarling, howling, enraged that it's chained and cannot move much.
    Unfortunately, the dog is blocking your way. It is standing right in the
    middle of the road.
    ''' 
    print(leftTurn)
    #NEW INPUT
    user_input2 = input("Type 'befriend' to befriend the dog or 'run' to try to run past the dog. ")
    if user_input2 == "befriend":
        befriend = '''
        Although you have always been scared of dogs ever since a dog bit you when you were little,
        you attempt to pet the dog's head. Slowly, you reach out your hand to pet the dog. "Maybe the dog
        is just lonely," you think, "Maybe that's why it's so angry." However, that doesn't seem to be the case.
        The dog bites your hand and you scream out in pain. 
        '''
        print(befriend)
        print(gameOver)
    elif user_input2 == "run":
        runAway = '''
        There's a small opening that you can run past if and only if you sprint past before the dog can realize
        what's happening. Since you used to be a track star in high school, you may have a chance to successfully
        run past and continue on with the maze. You take a deep breath and sprint past the barking dog. You made
        it! But then, you hear something... The dog is now in front of you. It must've broken the chain. Luckily,
        the dog is now panting happily since it is free.
        As you walk, the dog follows you. You and the dog come across another fork in the road. The dog
        seems eager to turn right, but the road on the left has flowers all over the wall and looks inviting.
        '''
        print(runAway)
        #NEW INPUT
        user_input3 = input("Type 'right' to go the way the dog wants and 'left' to follow the flowers. ")
        if user_input3 == "right":
            rightTurn2 = '''
            You decide to listen to the dog, even though you just met it minutes ago. You cautiously turn
            right, expecting to find another vicious dog. Instead of another dog, there is simply a door
            hidden in the ivy. It looks shady and very suspicious. The dog can't stop barking at the door.
            '''
            print (rightTurn2)
            #NEW INPUT
            user_input4 = input("Type 'open' to open the door and 'avoid' to avoid the door. ")
            if user_input4 == "open":
                print (win)
            elif user_input4 == "avoid":
                print (noTime)
                print (gameOver)
            else:
                user_input4 = input("Please only type 'open' or 'avoid'. ")
        elif user_input3 == "left":
            flowers = '''
            You walk through the flower path, but there's nothing there except flowers. It turns out you
            made a mistake not listening to the dog.
            '''
            print(flowers)
            print(gameOver)
        else:
            user_input3 == input("Please only type 'right' or 'left'. ")
    else:
        user_input2 = input("Please only type 'befriend' or 'run'. ")

        
elif user_input == "right":
    rightTurn = '''
    You choose to go right and you take many confusing turns in the maze while staying
    careful to avoid the walls. You're exhausted, dehydrated, and hungry.
    It feels like there's no hope left. Suddenly, you see something hidden in the ivy
    on the walls of the maze. It's charcoal black and as hard as a rock.
    As you uncover the ivy, the black object seems to be in the shape of
    a rectangle. Maybe it's a door! Rapidly, you keep pulling
    away the ivy to find the door knob.
    '''
    print (rightTurn)
    #NEW INPUT
    user_input5= input("Type 'door' to open the door and 'avoid' to keep going. ")
    if user_input5 == "door":
        print(win)
    elif user_input5 == "avoid":
        print(noTime)
        print(gameOver)
    else:
        input("Please only type 'door' or 'avoid'. ")
else:
    user_input = input("Please only type 'left' or 'right'. ")
   
