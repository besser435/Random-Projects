import time, pydirectinput, mouse, keyboard #,pyautogui
from time import sleep
# https://learncodebygaming.com/blog/pyautogui-not-working-use-directinput

# time in seconds before pick refill. 4000 seems to be right for Unbreaking III
REFILL_DELAY = 4450 #4450

refill_counter = 0

def refill_picks():
    # move to the dohickey
    pydirectinput.keyDown("s")
    sleep(2)
    pydirectinput.keyUp("s")
    pydirectinput.keyDown("d")
    sleep(3)
    pydirectinput.keyUp("d")

    # discard hotbar items
    for i in range(0, 9):
        pydirectinput.keyDown("ctrl")
        pydirectinput.press("q")    # assumes q is your drop items key
        pydirectinput.keyUp("ctrl")
        mouse.wheel(-1) # cycle hotbar slots. 
        # Would have liked to use a for loop and just hit the slot key (1-9) with the loop index rather than using the scrollwheel,
        # but it skipped slots for some reason. This is the next best thing.

    sleep(0.5)

    # dispense 9 new picks and equip them in the hotbar slot
    for i in range(0, 9):
        pydirectinput.click(button="right") # signals the machine to drop a pick
        mouse.wheel(-1) 
        sleep(0.5)

    sleep(0.5)

    # move to the money machine
    pydirectinput.keyDown("a")
    sleep(1)
    pydirectinput.keyUp("a")

    pydirectinput.keyDown("w")
    sleep(1.5)
    pydirectinput.keyUp("w")

    sleep(0.5)

try:
    print("Starting in 3 seconds...")
    sleep(3)
    print("Mining...")

    initial_time = time.monotonic()

    while True: 
        current_time = time.monotonic()
        time_stamp = int(current_time - initial_time + 1)    # +1 to not trigger refill_picks() on the first loop
       
        pydirectinput.mouseDown()
        mouse.wheel(-1)             # cycle through picks in hotbar
        pydirectinput.press("a")    # timeout prevention
        sleep(1)

        # if 4000, refills picks every 1.11 hours (about the time a pick lasts)
        if (time_stamp) % REFILL_DELAY == 0: 
            pydirectinput.mouseUp()
            refill_picks()
            refill_counter += 1
            print("Refilled")
        
        print("Refill in", REFILL_DELAY - (time_stamp % REFILL_DELAY), "seconds")

        if keyboard.is_pressed("f7"):
            raise KeyboardInterrupt
        pydirectinput.failSafeCheck()  # checks if mouse is in top left corner. If so, raises pydirectinput.FailSafeException and stops everything

except KeyboardInterrupt:
    end_time = time.time()
    pydirectinput.mouseUp()
    print("Done Mining")
    print("Time elapsed:", round((time_stamp / 3600), 2), "hours")
    print("Refilled picks", refill_counter, "times")
    input("\nPress enter to exit...")
