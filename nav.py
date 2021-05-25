  # Level 2
        #Navagate to the planet Python
"""this is a variation of the Ancient Game of Nimm from Assignment 2"""
        #intro and instructions
"""Help Karel reach Python safely"""
import random
        #write code



def play_level2():
        player = 1
        clicks = 20
        print("Help Karel land safely on planet Python\n")
        while clicks > 0:
                if player == 1:
                        print("The engine malfunctioned!")
                        user_input = int(input("Player enter 1 or 2: "))
                        while user_input != 1 and user_input != 2:
                                user_input= int(input("Please enter 1 or 2: "))
                        clicks -= user_input
                        if clicks >= 0:
                                print("There are ", str(clicks), " clicks left\n")
                                player = 2
                        else:
                                print("You MISSED the Planet!!!")
                else:
                        if clicks > 2: 
                                game_input = random.randint(0,2)
                                if game_input == 0:
                                        player = 1
                                else:
                                        print("The engine is working...!")
                                        print("the engine moved ", str(game_input), " clicks!")
                                        clicks -= game_input
                                        print("There are ", str(clicks), " clicks left\n")
                                        player = random.randint(1,2)
                        else:
                                player = 1

                
        print("You have made it to planet Python!")       
          



        #write error messages
        #write succes message
        #play again or move to next level