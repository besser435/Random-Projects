import board
import random
import os
from time import sleep
import adafruit_vl53l0x 
import adafruit_bh1750
#pip3 install adafruit-circuitpython-vl53l0x
#https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout/python-circuitpython
from adafruit_motorkit import MotorKit

i2c = board.I2C()

# Time of Flight LIDAR Sensors
tof0 = adafruit_vl53l0x.VL53L0X(i2c)
tof0.measurement_timing_budget = 100000 # 200000 is the default, 200ms

# Ambient light sensor
amb_light = adafruit_bh1750.BH1750(i2c)

# Motor driver
kit = MotorKit()

# Options
avoid_threshold = 200 # distance in mm before turning
turn_speed = 0.5
headlight_threshold = 200


def cc():   # shortens this long command to just cc()
    os.system("cls" if os.name == "nt" else "clear")    # clears terminal
cc()


def stop():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0


def motor(move_type, speed):
    """ def motor(move_type, speed, accel_time):
    gradually increases motor speed to the throttle value
    acceleration = 0 speed to desired speed in X amount of seconds
    not implemented yet. it might not need to be."""
    
    
    if move_type == "for":
        kit.motor1.throttle = speed
        kit.motor2.throttle = speed

    elif move_type == "back": 
        kit.motor1.throttle = -speed
        kit.motor2.throttle = -speed

    elif move_type == "left": # uses tank steering
        kit.motor1.throttle = turn_speed
        kit.motor2.throttle = -turn_speed

    elif move_type == "right":
        kit.motor1.throttle = -turn_speed
        kit.motor2.throttle = turn_speed



# https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/index.html
# https://docs.circuitpython.org/projects/tca9548a/en/latest/examples.html
def menu():
    print("Select move type: ")
    print("1. Object Avoidance") # could use both sensors to steer in most open direction, or use 
    # 1 to just detect, then change course
    print("2. Follow At Fixed Distance")
    print("3. Speed Up Gradually")
    print("4. Random")
    print("5. Remote Control")


"""def headlight(): # this should be a thread
    while True:
        if amb_light.lux < headlight_threshold:
            print("Low Light detected")
            #light strip on
        else:
            #lights off
        print("%.2f Lux" % amb_light.lux)
        sleep(2)"""


def object_avoidance(): # uses two sensors to detect the best direction to go
    while True:
        # average of both sensors
        lid0 = tof0.range #fetch range

        cc()
        print("Range: {}mm".format(lid0))


        
        motor("for", 1)

        # get range (both sensors averaged)
        # if range is less than avoid_threshold, turn towards the sensor that is further away
        # if range is greater than avoid_threshold, continue forwards

        if lid0 < avoid_threshold:
            print("Object detected")
  
                    



def follow_at_distance():
    follow_dist = 80 # distance to keep to the object in mm
    
    while True:
        lid0 = tof0.range
        
        cc()
        if lid0 < headlight_threshold + 2 or lid0 < avoid_threshold - 2:    # checks that the robot is whthin 2mm of object threshold
            print("Range: {}mm".format(lid0))
            print("Moving backwards")
            motor("back", 1)

        elif lid0 > headlight_threshold + 2 or lid0 > avoid_threshold - 2:
            print("Range: {}mm".format(lid0))
            print("Moving forwards")
            motor("for", 1)


        

        








def old(): 
    avoid_dir = ("left", "right")   
    random_avoid_dir = random.choice(avoid_dir) 
    
    # boot up animation
    # while this is set to turn for 1 second,
    # it could use a magnetometer to determine the starting position and return to that
    motor(random_avoid_dir, 1)  # boot up animation
    sleep(1)
    stop()
        
    while True:
        while not tof0.data_ready:
            pass
        tof0.clear_interrupt()
        range0 = tof0.distance # this is in centimeters
        print("Distance: {} cm".format(range0))

    

        motor("for", 1)

        # prints status info about what the robot is doing
        print("Moving ")
        print("Range to object: {} cm".format(range0))


        if range0 < avoid_threshold:
            print("Yo mama detected")
            stop() # might not be needed
            
            motor(random_avoid_dir, 1)
            if range0 > avoid_threshold + 1:    # scans for a new route
                motor("for", 1)
            else:
                print("Error - stuck. add a feature where it keeps turning until it finds a new route")
                #break

    
    
print("main() done")



