print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice1 = input("You\'re at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()

if choice1 == 'left':
    # continue
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat or Type \"swim\" to swim accross\n").lower()
    if choice2 == 'wait':
        # continue
        choice3 = input("You arrive at the Island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 == 'red':
            print("It's a room full of fire. Game Over")
        elif choice3 == 'yellow':
            print("You found the treasure! You Win!")
        elif choice3 == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over")
else:
    print("You fell into a hole. Game Over.")
    
