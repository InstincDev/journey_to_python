
"""This is a game created as a final project for Code in Place 2021
In this game Karel the robot wants to get from his world to the planet Python.
Users will help him:
* collect the supplies he needs for his trip
* make sure that karel's rocket weights the correct amount
* navagate to the planet Python
* create a unique gift for the Pythonistas

Users will gain practice using the skills learned in CiP 2021"""

from packing_karel import *
from nav import *
from python_gift import *


# Create console version of the game
def main():
    pass
    
    #Welcome Message
    #create welcome message
    print("Journey to Python")
    # var to hold user name
    name = input("Please enter your name: ")
    print("Welcome " + name + "!")
    print("In this game you will help Karel the robot journey from his world to the planet Python!\n")
    # Level 1
    # Help Karel collect for his trip
    """this is a variation of Hospital Karel from Section 1"""

    # Level 2
    #Navagate to the planet Python
    """this is a variation of the Ancient Game of Nimm from Assignment 2"""
    play_level2()
    # Level 3
    #Create a unique gift for the Pythonistas
    """this is a variation of Worhol Effect from Assignment 3"""
    play_level3()

    
        #intro and instructions
        #get image of Karel
        #create world
        #set beepers (supplies) that need to be collected
        #download image of Karel (save for later)
        #write code for Lvl 1
        #write error messages
        #write success message
        #play again or move to next level




   
        #intro and instructions
        #write code
        #write error messages
        #write success message
        #play again or move to next level

    
        #learn worhol effect 
        #design image
        #write code
        #write error message
        #write success message
        # play again

    # End
        #write closing message

if __name__ == '__main__':
    main()
