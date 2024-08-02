"""
This program is for lab 11 for CS21 focusing on Classes.

Constructor
    Takes in Adventurer's Name, Quest, Food, and Equipment.
    Store as instance variables
    Initialize variables of how many times adventurer has done something

Get Name (S)
    Return adventurer's name

_STR_ (S)
    Return a string that report ass the instance variables
        Must return name of each instance variable and value of 
        each instance variable
    This is a checking function.
    
Quest (S)
    Updates adventurer's state
        Increase quest by 1
        Decrease food by 1
    Print a message of what's happening
        Advenuter is activitying
    Cannot happen if the adventurer has not eaten. 
        Print out they need to eat
    
Eat (S)
    Updates adventurer's state
        Increase food by 1
    Print a message of what's happening 
        Adventurer is eating food
    Can only eat twice
        Print they cannot eat

Shop (S)
    Updates adventurer's state
        Increase equipment by 1
    Print a message of what's happening
        Adventurer got equipment  

Rest 
    Updates adventurer's state
        Decrease food by 1
        Decrease adventure by 1
    Print a message of what's happening
        Adventurer rests

Status (S)
    Return string with a description of Adventurer's state
        Print adventuer name and what they're current state is based on counter
     
"""


class Adventurer:
    def __init__(self, name, quest, food, equipment):
        """
        Creates the instances like name, quest, food, equipment
        Refer to constructor in TDD
        Parameter: 
            self = Itself
            name (str) = name of adventurer
            quest (str) = fav quest
            food (str) = fav food
            equipment (str) = fav equipment
        Return: self.name (str)= Name of adventurer
        Side Effects: Nothing
        """
        #Instances
        self.name = name
        self.favquest = quest
        self.food = food
        self.equipment = equipment
        #Counters
        self.tfood= 0
        self.tquest= 0
        self.tequip= 0

    def get_name(self):
        """Gets Adventurer name
        Refer to name in TDD.
        Parameter: self = Itself
        Return: self.name (str)= Name of adventurer
        Side Effects: Nothing
        """
        return self.name
    
    def __str__(self):
        """
        Lists out what the instance created is. Esstentially, a print statement
        Refer to TDD str
        Parameter: self = Itself
        Return: print statement
        Side Effects: Nothing
        """
        return "Adventurer's name is %s. He likes to %s. \
He likes to eat %s. His fav equipment is %s." \
                % (self.name, self.favquest, self.food, self.equipment)

    def quest(self):
        """Quests the adventurer and prints statement
        Refer to quest in TDD.
        Parameter: self = Itself
        Return: Nothing
        Side Effects: Prints statement, increases quest, lowers food
        """
        if self.tfood > 0:
            self.tfood -= 1
            self.tquest += 1
            print(self.name + " is " + self.favquest + " .")
        elif self.tfood < 1 :
            print(self.name + " has to eat first!")

    def eat(self):
        """Feeds the adventurer and prints statement
        Refer to eat in TDD.
        Parameter: self = Itself
        Return: Nothing
        Side Effects: Prints statement, adds food intake
        """
        if self.tfood == 0 or self.tfood == 1:
            self.tfood += 1
            print(self.name + "is eating some " + self.food + ".")
        if self.tfood >= 2:
            print(self.name + " is full!")
            
    def shop(self):
        """Equipes the adventurer and prints statement
        Refer to shop in TDD.
        Parameter: self = Itself
        Return: Nothing
        Side Effects: Prints statement, adds equip
        """
        self.tequip += 1
        print(self.name + " has equiped backback!")

    def rest(self):
        """Rests the adventurer and prints statement
        Refer to rest in TDD.
        Parameter: self = Itself
        Return: Nothing
        Side Effects: Prints statement, lowers quest, lowers food
        """
        if self.tfood > 0:
            self.tfood -= 1
        if  self.tquest > 0:
            self.tquest -= 1
        print(self.name + " is well rested!")
    
    def status(self):
        """Prints the what's the scenario of the Adventurer
        Parameter: self = Itself
        Return: Nothing
        Side Effects: Prints statements based on scenario
        """
        print("Adventurer: " + self.name + " is ")

        if self.tfood > 0:
            if self.tfood == 1:
                print ("Well Fed with food    " + "||| Times Eaten: " \
+ str(self.tfood))
            else:
                print ("OVER Fed with food     " + "||| Times Eaten: " \
+ str(self.tfood))
        else:
            print("STILL Hungry with food     " + "||| Times Eaten: "\
+ str(self.tfood))

        if self.tquest > 0:
            if self.tquest == 1:
                print ("Well Content with quests    " + "||| Times Quested: " \
+ str(self.tquest))
            else:
                print ("OVER Content with quests    " + "||| Times Quested: " \
+ str(self.tquest))
        else:
            print("NOT Content with quests    " + "||| Times Quested: " \
+ str(self.tquest))

        if self.tequip > 0:
            print ("has his equipment.    " + "||| Current Equips: "\
+ str(self.tequip))
        else:
            print("has NOT his equipment.    " + "||| Current Equips: "\
+ str(self.tequip))




def main():
    x = Adventurer("ben", "hike", "pizza", "bike")
if __name__ == "__main__":
  # only call main if we run this file directly
  # don't call main when we import this file
  main()
