"""
functions aka methods
    an action on something
    
    string methods
    list methods
    
actions on _____ (string, list, etc)

a method aka function actions data (values and therefor data type)

if a list/tuple/set/dictionary is a collection/series of values

a method is a collection or series of actions (steps to take)
"""


def sleep(where, noise_level):
    
    heart_rate = "slow"
    if where == "bed" and noise_level < 30:
        eyes_open = False
    elif where == "bed":
        eyes_open = True
    else:      
        eyes_open = True
        heart_rate = "normal"
    return {"heart_rate": heart_rate, "eyes_open": eyes_open}


value = sleep("train", 100)
print(value)
