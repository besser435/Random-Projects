import time
import ntplib
import os

import busio
#import board
#import adafruit_veml7700
import neopixel



DISPLAY_BRIGHTNESS = 1
SHUTOFF_LUX_THRESHOLD = 10

H_COLOR = (255, 0, 0)
M_COLOR = (0, 255, 0)
S_COLOR = (0, 0, 255)


# Hardware setup
#i2c = busio.I2C(board.SCL, board.SDA)
#veml7700 = adafruit_veml7700.VEML7700(i2c)
#led_neo = neopixel.NeoPixel(board.D18, 1)



def binary_time():
    # Create an NTP client
    """    
    https://www.ntppool.org/en/tos.html
    Dont set more often than every 30 minutes
    try:
            client = ntplib.NTPClient()
            response = client.request("pool.ntp.org")

            # Get the current time from the response
            current_time = time.localtime(response.tx_time)
        except Exception as e:
            print("Error: ", e)"""
    current_time = time.localtime()


    hours = current_time.tm_hour
    mins = current_time.tm_min
    secs = current_time.tm_sec

    bin_hours = bin(hours)[2:].zfill(6) # NOTE must match pixel count for each time unit
    bin_mins = bin(mins)[2:].zfill(6)
    bin_secs = bin(secs)[2:].zfill(6)
    print(bin_hours, bin_mins, bin_secs)

    return bin_hours, bin_mins, bin_secs


def light_shutoff():    # turns the display off if it's dark, like when you're sleeping
    lux = veml7700.lux
    light = veml7700.light
    print("Lux:", lux)
    print("Ambient Light:", light)


    if lux < SHUTOFF_LUX_THRESHOLD:
        led_neo.brightness = 0
    else:
        led_neo.brightness = DISPLAY_BRIGHTNESS
        

def paint_display():
    """
    Hour, minute, second each get 6 bits/pixels for the 
    binary display.
    
    """

    bin_hours, bin_mins, bin_secs = binary_time()
    binary_values = bin_hours + bin_mins + bin_secs
    # count the number of chars in the binary string
    print("binary length",len(binary_values))
    
        
    for i in range(18):
        #print(binary_values)

        if i < 6:
            target_color = H_COLOR if binary_values[i] == '1' else (3, 3, 3)
        elif i < 12:
            target_color = M_COLOR if binary_values[i] == '1' else (2, 2, 2)
        else:
            target_color = S_COLOR if binary_values[i] == '1' else (1, 1, 1)
        #led_neo[i] = target_color
        print(target_color)



        """
        FADE_DURATION = 0.25  # Duration of the transition in seconds
        current_color = led_neo[i]
        step_count = int(FADE_DURATION * 10)  # Number of steps in the transition

        for step in range(step_count):
            # Calculate the color at the current step in the transition
            fraction = (step + 1) / step_count
            intermediate_color = tuple(
                int((1 - fraction) * current + fraction * target)
                for current, target in zip(current_color, target_color)
            )

            led_neo[i] = intermediate_color
            time.sleep(FADE_DURATION / step_count)

        led_neo[i] = target_color  # Set the final color"""


    

while True:
    paint_display()
    #light_shutoff()

    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

