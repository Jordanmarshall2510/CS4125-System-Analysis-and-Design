#Coded by Jakub Pazej - 18260179
import json
import os
import time

class Clock():
    time=0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("World")[0] + "config.json"
        
        with open(path) as json_file:
            conf = json.load(json_file)
        self.time=time.mktime(time.strptime(conf['world']['clock']['date'], '%d.%m.%Y, %H:%M:%S'))

    def getTime(self):
        return time.strftime("%A, %d.%m.%Y, %H:%M:%S",time.localtime(self.time))

    def getTimeOnly(self):
        return time.strftime("%H:%M:%S",time.localtime(self.time))

    def getTimeHours(self):
        return time.strftime("%H",time.localtime(self.time))

    def getTimeMinutes(self):
        return time.strftime("%M",time.localtime(self.time))

    def getTimeSeconds(self):
        return time.strftime("%S",time.localtime(self.time))

    def getTimeSeconds(self):
        return self.time

    def setTime(self, string):
        try:
            self.time=time.mktime(time.strptime(string, '%d.%m.%Y, %H:%M:%S'))
        except Exception as e:
            print("Wrong input!!!")

    def setTimeSeconds(self, value):
            self.time=value

    def checkDaylight(self):
        if(8<int(self.getTimeHours()<18)):
            return True
        else:
            return False