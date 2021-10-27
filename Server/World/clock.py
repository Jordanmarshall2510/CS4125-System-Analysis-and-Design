#Coded by Jakub Pazej - 18260179
import yaml
import time
from World.weather import *

# Whether it night time.
NIGHT_TIME = False

class Clock():
    time=0

    def __init__(self):
            with open('config.yaml', 'r') as f:
                config = yaml.load(f, Loader = yaml.FullLoader)
            self.time=time.mktime(time.strptime(config['world']['clock']['date'], '%d.%m.%Y, %H:%M:%S'))

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
