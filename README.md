# Adventurer-Game


In this lab, I created a simple class to represent a team of Adventurers who love going on quests! Each Adventurer was described by the Adventurer class. My program consisted of two files:

adventurer.py contained the class definition for the Adventurer class, and
team.py contained a program that allowed me to take the Adventurers on quests.
Adventurers are characters in a fictional world who enjoy adventures. Each Adventurer had a favorite quest to go on. For example, Barney liked to chase dragons. However, Adventurers couldn’t go on quests on an empty stomach, so before setting off, they needed to eat. Barney’s favorite food was purple grapes, so before chasing dragons, Barney would eat purple grapes. After eating and questing, Barney might want to buy some purple hiking boots before heading out on another quest. And after a long day of eating purple grapes, chasing dragons, and shopping for new hiking boots, Barney would want to rest.

In this part of the lab, I needed to import the Adventurer class into my team.py program by writing from adventurer import * at the top of the team.py file. As long as adventurer.py was in the same directory, this import statement was enough for Python to find the file and pull in the Adventurer class definition. It was important to note that I imported from adventurer, not adventurer.py, since Python knows to add the .py automatically when looking for the file.

The program in team.py implemented a menu loop similar to those in previous labs, with options for taking the Adventurers on a quest. I stored all of my Adventurers in a list of Adventurer objects, which was initially empty when the program started. The menu allowed me to perform several actions on the team of Adventurers.
