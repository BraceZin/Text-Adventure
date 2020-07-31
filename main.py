print("Hello, Welcome to Text Adventure!")
age = input("How old are you (Please type in a number)? ")
health = 10
if age >= "10":
    print("You are old enough to play!")
    consent = input("Do you want to play? ").lower()
    if consent == "yes":

        print("You are starting with", health, "health!")
        print("Let's play!")
        #start game
        left_or_right = input(
            "First choice, do you want to go left or right (left/right)? ")
        if left_or_right == "left":
            ans = input(
                "Nice! You follow the path and reach a lake...do you swim across or go around (across/around)? "
            )
            if ans == "around":
                print(
                    "You went around and reached the other side of the lake!")
            elif ans == "across":
                print(
                    "You managed to get across, but you were bit by a fish and lost 5 health."
                )
                health -= 5

            ans = input(
                "You notice a house and a river. Which do you go to (river/house) "
            )
            if ans == "house":
                print(
                    "You enter the house and are greeted by the owner...He doesn't like you and you lose 5 health!"
                )
                health -= 5
                if health <= 0:
                    print('You know have 0 health and you lost the game...')
                else:
                    print("You have survived...you win!!!")
            else:
                print("You fell down a river and lost... ")
        else:
            print("You fell down a cliff and lost...")
    else:
        print("See ya later....")
else:
    print("You are not old enough to play...")

#STUFF TO ADD
  # Weapons -> Be able to defeat villains based on weapons strength
  # Villiams -> Be able to have health and keep defeating
  # Common Items -> Being able to call people, drink water, eat
  # Dehydration -> Able to check for dehydration
  # Hunger -> Able to check for starvation