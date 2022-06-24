# Simon Says
from colorama import init
init()
from colorama import Fore
init(autoreset=True)
import random
import os


def cc():   # shortens this long command to just cc()
    os.system("cls" if os.name == "nt" else "clear")    # clears terminal
cc()


def main():
    memory = []
    colors = [Fore.LIGHTRED_EX + "Red", Fore.LIGHTCYAN_EX + "Blue", Fore.LIGHTGREEN_EX + "Green", Fore.LIGHTYELLOW_EX + "Yellow"]
    rand_color = random.choice(colors)
    print(rand_color)

    def sequence():
        memory.append(random.choice(colors))
        print(memory)
        print("Press the correct button")
        
    sequence()


def menu():
    print("Simon Says game")
    print("1. Play game")

    #ask = input("")
    #if ask == "1":
    cc()
    main()

menu()

