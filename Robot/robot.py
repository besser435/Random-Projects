from xml.etree.ElementTree import TreeBuilder
import board
import random
from time import sleep
import adafruit_vl53l4cd
from adafruit_motorkit import MotorKit

i2c = board.I2C()

# Time of flight sensor
tof0 = adafruit_vl53l4cd.VL53L4CD(i2c)
tof0.inter_measurement = 0
tof0.timing_budget = 100 # 200 is the default. 

tof1 = adafruit_vl53l4cd.VL53L4CD(i2c) # change to the right address!
tof1.inter_measurement = 0
tof1.timing_budget = 100 # 200 is the default. 

# Motor driver
kit = MotorKit()

# Options
avoid_threshold = 4 # distance in centimeters before turning
turn_speed = 0.5

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
        # left but inverted motor values
        pass



def prototype_movement():
    # rather than just moving forwards until it hits something,
    # the robot could just turn to where it has more space. then it runs the 
    # collision avoidance bit if it detects that the distance is less than the avoid_threshold.

    # It might jitter a bit from the sensors not matching perfectly, so if the distance to an
    # object is more than X, just make it go forwards. rather than the above movement method.
    # Or you could just make it so that the two sensors must differ by a certain amount before it steers.
    

    # to have 2 sensors, they would need to have different I2C addresses. you cant change the I2C address on them.
    pass


def main(): 
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



