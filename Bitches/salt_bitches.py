"""
Bitches.py uses your name as a seed for an RNG to see how many bitches you get.
This finds a salt to make your name result in zero bitches.
"""

import random

salt = 0
name = input("Enter your name: ")

def get_bitches():
    random.seed(name + str(salt))
    #print("salt used: " + str(salt))
    return random.randint(0, 10)
UNSALTED_BITCHES = get_bitches()   

# tests each salt starting from 0 until the name plus salt returns 0 bitches
while get_bitches() > 0:    
    salt += 1
   
print("Salt to return '" + str(name) + "' with 0 bitches is " + str(salt))

# "without a salt" means the default salt in this file. Not actually no salt
print("Without a salt, '" + str(name) + "' will return with " + str(UNSALTED_BITCHES) + " bitches") 
input("Press enter to close")