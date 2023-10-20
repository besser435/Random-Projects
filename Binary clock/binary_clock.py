import time
"""
Ideas:
Use ambient light sensor to turn the display off when it's dark


"""



# get the current time in format HH:MM:SS
current_time = time.strftime("%H:%M:%S", time.localtime())
print(current_time)

#convert hours into binary
hours = int(current_time[0:2])
print(hours)
hours = "{0:b}".format(hours)
print(hours)
