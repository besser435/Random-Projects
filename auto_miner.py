import time, pyautogui

times_clicked = 0
money_lost = 0
start_time = time.time()
try:
    print("Clicking...")
    while True:
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()

        time.sleep(2.5)
        times_clicked += 1
        money_lost += 5.2

except KeyboardInterrupt:
    end_time = time.time()
    print("Done clicking")
    print("Money lost:", money_lost)
    print("Clicked " + str(times_clicked) + " times")
    print("Time elapsed:", (end_time - start_time) / 3600, "hours")
    input("\nPress enter to exit...")
