from characters import Fighters
from fight import Fight

# Set user character name
usr_char_name = input("Enter character name: ")

# Objects/Instances
fighter1 = Fighters(usr_char_name, 100)
fighter2 = Fighters("Someone", 100)

fight = Fight(fighter1, fighter2)
fight.start()

# The real Result
if fighter1.getHealth() > 0 and fighter2.getHealth() <= 0:
    print("You're lucky, and you don't get to pay for lunch today!")
elif fighter1.getHealth() <= 0 and fighter2.getHealth() <= 0:
    print("It's a tie so Play again")
else:
    print("Too bad... You aren't as lucky as usual today... Now pay for my lunch!\nNow choose one of the dishes that you'll treat me with\n1. Biryani\n2. Chaat\n3. Nihari")

