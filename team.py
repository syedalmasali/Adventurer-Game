"""
This program uses the adventurer class I created and implements a fun game.

Adventurer goes on adeventures.
    Need a function for questing
Each adventurer has favorite everything.
    Going to use the classes to get these
    need inputs
Adventurers cannot go to quests on empty stomach.
    Going to use the classes to get these inputs
Adventurers need to shop before going on quests.
    Going to use the classes to get these inputs
Adenturer can shop as much as he wants
    Going to use the classes to get these inputs
Adventurers should rest after awhile.
    Going to use the classes to get these inputs

Not that much coding as the classes file already does everything that
is needed. Most of the coding is basically print statements

"""
#Imports the class Adventurer
from adventurer import Adventurer


def reportstatus(players):
    '''
    Reports the current status of the player.
    Parameters: 
        players (lst) = list of all the adventurers as objects
    Returns:
        Nothing
    Side Effects:
        Prints some statements based on current conditions
    '''
    #If the list is empty, have to recruit players first
    if players == []:
        print("Have to recruit players!")
        print("")
    #print status for each person in list
    for i in range(len(players)):
        players[i].status()
    

def recruit():
    '''
    Creates an adventurer
    Parameters: 
        Nothing
    Returns:
        x (Adventurer)= the new adventurer
    Side Effects:
        Prints some statements based on current conditions
        Takes in some inputs
    '''
    #base inputs
    name = input("What is the name of your adventurer? ")
    activty = input("What is his favority hobby? ")
    food = input("What is his favorite food? ")
    equipment = input("What is his favorite piece of equipment? ")
    #create adventurer
    x= Adventurer(name, activty, food, equipment)
    #print t=what they like to do
    print(x)
    #return the adventurer
    return x


def questing(players):
    '''
    Takes the adventurer out to quest.
    Parameters: 
        players (lst) = list of all the adventurers as objects
    Returns:
        Nothing
    Side Effects:
        Prints some statements based on current conditions
    '''
    #If the list is empty, have to recruit players first
    if players == []:
        print("Have to recruit players!")
        print("")
    else:
        #associates index to adventurer
        for i in range(len(players)):
            print(players[i].get_name() + " is the number " + str(i))
        #Picks the adventurer and does the activtity
        thechoice = input("What adventurer to quest \
(Input corresponding number)? ")
        players[int(thechoice)].quest()


def feed(players):
    '''
    Feeds the adventurer.
    Parameters: 
        players (lst) = list of all the adventurers as objects
    Returns:
        Nothing
    Side Effects:
        Prints some statements based on current conditions
    '''
    #If the list is empty, have to recruit players first
    if players == []:
        print("Have to recruit players!")
        print("")
    else:
        #associates index to adventurer
        for i in range(len(players)):
            print(players[i].get_name() + " is the number " + str(i))
        #Picks the adventurer and does the activtity
        thechoice = input("What adventurer to feed (Input corresponding \
number)? ")
        players[int(thechoice)].eat()


def shopping(players):
    '''
    Takes the adventurer out to shop.
    Parameters: 
        players (lst) = list of all the adventurers as objects
    Returns:
        Nothing
    Side Effects:
        Prints some statements based on current conditions
    '''
    #If the list is empty, have to recruit players first
    if players == []:
        print("Have to recruit players!")
        print("")
    else:
        #associates index to adventurer
        for i in range(len(players)):
            print(players[i].get_name() + " is the number " + str(i))
        #Picks the adventurer and does the activtity
        thechoice = input("What adventurer to take shopping (Input \
corresponding number)? ")
        players[int(thechoice)].shop()


def resting(players):
    '''
    Takes the adventurer out to rest.
    Parameters: 
        players (lst) = list of all the adventurers as objects
    Returns:
        Nothing
    Side Effects:
        Prints some statements based on current conditions
    '''
    #If the list is empty, have to recruit players first
    if players == []:
        print("Have to recruit players!")
        print("")
    else:
        #associates index to adventurer
        for i in range(len(players)):
            print(players[i].get_name() + " is the number " + str(i))
        #Picks the adventurer and does the activtity
        thechoice = input("What adventurer to rest (Input corresponding \
number)? ")
        players[int(thechoice)].rest()


def playgame():
    '''
    Main function of the game. Big while loop that keeps asking
    the next move. Calls all the other functions.
    Parameters: 
        Nothing
    Returns:
        Nothing
    Side Effects:
        Prints some statements based on current conditions
        Takes in some inputs
    '''
    #intializes a variable to track players
    players= []
    #keep asking prompt until invalid
    condition = True
    while condition == True:
        print("Main Menu: \n"
            "1. Report the status of the adventurers \n"
            "2. Recruit a new adventurer \n"
            "3. Take an adventurer on a quest \n"
            "4. Feed an adventurer \n"
            "5. Shop for an adventurer \n"
            "6. Rest for the night \n"
            "0. Quit")
        choice = input("What do you want to do? ")
        #what to do if choice 1
        if choice == "1":
            reportstatus(players)
        #what to do if choice 2
        elif choice == "2":
            player = recruit()
            #appends the new player
            players.append(player)
        #what to do if choice 3
        elif choice == "3":
            questing(players)
        #what to do if choice 4
        elif choice == "4":
            feed(players)
        #what to do if choice 5
        elif choice == "5":
            shopping(players)
        #what to do if choice 6
        elif choice == "6":
            resting(players)
        #what to do if choice 0
        elif choice == "0":
            print("Thank you for playing!")
            #Break out the loop
            condition = False


def main():
    '''
    Does literally nothing but calling the play game.
    Kept it like this ebcause what if later on we need 
    to import this file for something
    Parameters: 
        Nothing
    Returns:
        Nothing
    Side Effects:
        Calls the playgame function
    '''
    #calls the play game
    playgame()

main()
