'''
Non Fun Token
It is that repulsive
Almost as much as ur mom
I actually have autism, don't blame me

The real way to do this is to use an API
to fetch a random NFT and just save it as 
an image, but I couldnt figure out how to
do stuff with the data I got back
smooth brain time

'''
from colorama import init                   # pip install colorama
init()
from colorama import Fore, Back, Style
init(autoreset=True)
from PIL import ImageGrab
import webbrowser                           
import PIL                                  # pip install pillow
import sys
import os
import keyboard                             # pip install keyboard

capture_key = "s"
save_name = "ctrl+c.png"

while True:
    os.system("cls" if os.name == "nt" else "clear")

    def cd():   # changes directory to where the .py file is to save image
        try:
            abspath = os.path.abspath(sys.argv[0])
            dname = os.path.dirname(abspath)
            os.chdir(dname)
        except:
            print(Fore.RED + "cd error")
    cd()


    def message():
        print(Fore.LIGHTGREEN_EX + "Free image finder by Besser")
        print()
        print("This will get you a free image, for FREE!")
        print("It is going to open an NFT website")
        print("Once it loads and NFTs are visible, hit " + capture_key)
        print("Step 4: Profit.")
        print("???")
        print()
    message()


    input(Fore.RED + "Hit enter to continue")

    webbrowser.open("https://opensea.io/assets", autoraise=True) # shows NFTs
    print("Loading...")


    def screenshot():
        image = ImageGrab.grab(bbox=())
        image.save(save_name)    # just copies the NFTs lol

        image = PIL.Image.open(save_name)
        image.show()             # shows NFTs to you for FREE! You now own an image for FREE!


    def end():
        os.system("cls" if os.name == "nt" else "clear")
        print("Congrats! You now own pixels that you didn't have to pay for!")
        print("Image saved in: " + os.getcwd())


    while True:     # thanks google
        try:        # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed(capture_key):  
                screenshot()
                end()
                break 
        except:
            break   # if user pressed a key other than the given key the loop will break
    redo = input("Another one? y/n ")
    if "y" in redo:
        pass
    else:
        break
