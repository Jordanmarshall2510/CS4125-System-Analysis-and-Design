#Coded by Jakub Pazej - 18260179
import json
import os
import time

"""TODO: Validate if this file can be removed if so remove it"""

class Clock():
    time=0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("World")[0] + "config.json"
        
        with open(path) as json_file:
            conf = json.load(json_file)
        self.time=time.mktime(time.strptime(conf['world']['clock']['date'], '%d.%m.%Y, %H:%M:%S'))

    def get_time(self):
        return time.strftime("%A, %d.%m.%Y, %H:%M:%S",time.localtime(self.time))

    def get_time_only(self):
        return time.strftime("%H:%M:%S",time.localtime(self.time))

    def get_time_hours(self):
        return time.strftime("%H",time.localtime(self.time))

    def get_time_minutes(self):
        return time.strftime("%M",time.localtime(self.time))

    def get_time_seconds(self):
        return time.strftime("%S",time.localtime(self.time))

    def get_time_seconds(self):
        return self.time

    def set_time(self, string):
        try:
            self.time=time.mktime(time.strptime(string, '%d.%m.%Y, %H:%M:%S'))
        except Exception as e:
            print("Wrong input!!!")

    def set_time_seconds(self, value):
            self.time=value

    def get_daylight(self):
        if(8<int(self.get_time_hours()<18)):
            return True
        else:
            return False