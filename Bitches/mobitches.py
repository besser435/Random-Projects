import random

max_bitches = 10
name = input("Enter your name: ")
random.seed(name)
bitches = random.randint(0, 10)

while bitches == max_bitches:
        bitches = random.randint(max_bitches, (max_bitches * 10))
        max_bitches = (max_bitches * 10)

if (bitches == 0) or (name == "Brandon"):
    print("Damn you get no bitches fr fr")
elif bitches == 1:
    print("Only 1 bitch?")
elif bitches > 6:
    print("Damn, you get loads of bitches. " + str(bitches) + ", to be precise.")
else:
    print("You get " + str(bitches) + " bitches")

input("Press enter to close")