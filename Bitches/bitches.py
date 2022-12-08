import random
salt = 0    # lets you alter the output of the RNG. Refer to salt_bitches.py
random.seed(input("Enter your name: ")+ str(salt)) 
bitches = random.randint(0, 10)

if bitches == 0:
    print("Damn you get no bitches fr fr")
elif bitches == 1:
    print("Only 1 bitch?")
elif bitches > 6:
    print("Damn, you get loads of bitches. " + str(bitches) + ", to be precise.")
else:
    print("You get " + str(bitches) + " bitches")

input("Press enter to close")