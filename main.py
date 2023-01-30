print("Welcome to my first game!")
name = input("What is your name? ") #prompts user to enter their name in the console
age = int(input("What is your age? ")) #prompts user to enter their age in the console. 
    #Note: Even though an int value is entered for age, by default it would be set as str because it is an input, 
    #hence wrapped in int() function

print("Hello", name, "you are", age, "years old.") #commas automatically add spacing between the string

health = 10

if age >= 18 :
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower() #nested in the if statement so only showing this input if they are old enough to play 
   #.lower function makes the input lowercase regardless of what the user enters 

    if wants_to_play == "yes" :                    #then they have this input if they want to play
        print("You are starting with", health, "health")
        print ("Let's play!")

        left_or_right = input("First choice...Left or Right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("Nice, you followed the path and reach a lake...Do you swim across or go around (across/around)? ").lower()

            if ans == "around" :
                print("You went around and reached the other side of the lake.")
            elif ans == "across" :
                print("You managed to get across but were bit by a fish and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house" :
                print("You go to the house and are greeted by the owner...he doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0 :
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You survived and won the game!")
            elif ans == "river" :
                print("You fell in the river and lost...")

        else:
            print("You fell down and lost... ")
    elif wants_to_play == "no" :
        print ("Ok, goodbye...")
else : 
    print("You are not old enough to play...")