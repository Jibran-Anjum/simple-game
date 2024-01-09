import random

class Characters:
    def __init__(self, name, health):
        
        # private Attributes
        self.__name = name
        self.__health = health

    # Getter method and Setter methods
    def getName(self):
        return self.__name
    def getHealth(self):
        return self.__health
    def setHealth(self, value):
        self.__health -= value

    def damageGiven(self, other):
        pass
    
    # update Health
    def damageTaken(self, damage):
        self.__health -= damage


class Fighters(Characters):

    # Class Attribute
    move = ""

    def __init__(self, name, health):
        super().__init__(name, health)
        self.moves_list = ["punch", "kick", "special move"]

    # Getter method for the class attribute "move"
    def getMove(self):
        self.move = self.moves_list[random.randint(0, 1)]

    # Setting damage that is to be subtracted from health
    def damageGiven(self, other):
        if self.move.lower() == "punch":
            other.setHealth(4)
        elif self.move.lower() == "kick":
            other.setHealth(6)
        elif self.move.lower() == "special move":
            other.setHealth(12)
