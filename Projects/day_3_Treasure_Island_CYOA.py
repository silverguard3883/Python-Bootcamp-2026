print("Welcome to Treasure Island!\nYour mission is to find the treasure.\nYour stand at a crossroads. Choose where you want to go.\n")
crossroads_choice = input("Type 'left' or 'right': ").lower() #.lower() function normalizes input into lowercase

if crossroads_choice == "left":
    print("You come across a stream. What do you do?")
    stream_choice = input("Type 'swim' or 'wait': ").lower()
    
    if stream_choice == "swim":
        print("You find a cabin with 3 doors: red, blue, and yellow.")
        door_choice = input("Which do you open?: ").lower()
        
        if door_choice == "yellow":
            print("You find that the real treasure was the friends we made along the way. You Win!")
        elif door_choice == "red":
            print("You fall into a firey doom. Game Over.")
        elif door_choice == "blue":
            print("You open the door and are eaten by a horse-sized goat. Game Over.")
        else:
            print(f"{door_choice} is not a valid choice. You had 3 options and didn't choose any of them. Rocks fall, you die. Game Over")

    else:
        print("While doing anything other than swimming, a trout leaps out of the river and impales you. Game Over.")
else:
    print("You fall into a hole and can't get out. Game Over.")