import json
import os
import sys
from datetime import datetime

def cd():   # changes directory to where the .py file is. for the audio
    try:
        abspath = os.path.abspath(sys.argv[0])
        dname = os.path.dirname(abspath)
        os.chdir(dname)
    except:
        print("cd error")
cd()

#NOTE THIS ONLY REMOVIES IT ONCE      
# maybe because it only does it for one object                             
"""def remove_non_games(): # removes Customs and The Range
    obj = json.load(open("valorant_match_history.json"))

    # Iterate through the objects in the JSON and pop (remove)                      
    # the obj once we find it.                                                      
    for i in range(len(obj)):
        if obj[i]["game_type"] == "Not Applicable":
            obj.pop(i)
            break

    # Output the updated file with pretty JSON                                      
    open("updated-file.json", "w").write(
        json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    )
    
remove_non_games()
"""

print("Fetching playtime (this may take a while)")
def get_val_playtime():
    obj = json.load(open("valorant_match_history.json"))
    total_playtime = 0
    for i in range(len(obj)):

        # get the times from the json file
        end_time = obj[i]["game_end_time_utc"]
        start_time = obj[i]["game_start_time_utc"]

        obj = json.load(open("valorant_match_history.json"))

        # convert the strings to datetime objects
        dt_end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        dt_start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")

        # calculate the difference between the two times
        difference = (dt_end - dt_start)
        game_seconds = difference.total_seconds()

    # fetch total playtime
        total_playtime += game_seconds
    print(total_playtime)
    
    # print total_playtime in hours, minutes, seconds
    hours = total_playtime // 3600
    minutes = (total_playtime % 3600) // 60
    seconds = (total_playtime % 3600) % 60
    print("Total playtime: " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds")


get_val_playtime()

input("Press Enter to exit")



