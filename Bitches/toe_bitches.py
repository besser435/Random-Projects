import random


members = [
    "brandonusa", "linus sex tips", "dairypig", "Saxboy_laFranks", "Theeno74", "HexdePixel", 
    "emu", "Nolan", "GeneticEmo", "emperor ducc", "__Leah", "Greenland", "IcYPoP", "Big Cheegus GENIE"
    ]
max_bitches = 10
results = {}


for player in members:
    random.seed(player)
    bitches = random.randint(0, 10)

    
    while bitches == max_bitches:
        bitches = random.randint(max_bitches, (max_bitches * 10))
        max_bitches = (max_bitches * 10)


    print(player + " gets " + str(bitches) + " bitches")
    results[player] = bitches
print("catisa gets 0 bitches ")


print()
print(results)
dict(sorted(results.items(), key=lambda item: item[1]))

print()
sorted_reults = sorted(results)
print(sorted_reults)



input("\nPress enter to close")
