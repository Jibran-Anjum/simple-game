import time

class Fight:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def start(self):
        print(f"Fight has started between \"{self.fighter1.getName()}\" and \"{self.fighter2.getName()}\"")

        # The actual fight
        while self.fighter1.getHealth() > 0 and self.fighter2.getHealth() > 0:
            self.fighter1.getMove()
            self.fighter2.getMove()
            print("--------------------------------------------------")
            print(f"Name - {self.fighter1.getName()}, Health - {self.fighter1.getHealth()}\nName - {self.fighter2.getName()}, Health - {self.fighter2.getHealth()}")
            self.fighter1.damageGiven(self.fighter2)
            self.fighter2.damageGiven(self.fighter1)
            time.sleep(1)

        # Result
        if self.fighter1.getHealth() <= 0 and self.fighter2.getHealth() > 0:
            print("--------------------------------------------------")
            print(f"\"{self.fighter2.getName()}\" won!<*_*>")
            print("--------------------------------------------------")
            print(f"\"{self.fighter1.getName()}\" lost <|_|>")
            print("--------------------------------------------------")
        elif self.fighter2.getHealth() <= 0 and self.fighter1.getHealth() > 0:
            print("--------------------------------------------------")
            print(f"\"{self.fighter1.getName()}\" won!<*_*>")
            print("--------------------------------------------------")
            print(f"\"{self.fighter2.getName()}\" lost <|_|>")
            print("--------------------------------------------------")
        elif self.fighter1.getHealth() <=0 and self.fighter1.getHealth() <=0:
            print("--------------------------------------------------")
            print(f"\"{self.fighter1.getName()}\" lost <|_|> And \"{self.fighter2.getName()}\" lost <|_|>")
            print(f"Which Means it's a tie!")
            print("--------------------------------------------------")
