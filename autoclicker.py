import time, pyautogui, random
from datetime import datetime

times_clicked = 0
start = datetime.now()
current_time = start.strftime("%H:%M:%S")

try:
    print("Started clicking at: ", current_time)
    while True:
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()
        time.sleep(2.5)

except KeyboardInterrupt:
    stop = datetime.now()
    current_time = stop.strftime("%H:%M:%S")
    print()
    print("Done clicking")
    print("Clicked " + str(times_clicked) + " times")
    print("Stopped clicking at: ", current_time)
    print("Elapsed time:", stop - start)
    input("\nPress enter to exit...")


