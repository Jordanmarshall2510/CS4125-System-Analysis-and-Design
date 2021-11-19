#Coded by Jakub Pazej - 18260179
import random
import json
import os
import time

from World.clock import Clock
from World.weather import Weather

class environment:
    delay=0
    weather_change=0
    clock= Clock()
    weather= Weather()
    start=False

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split(" World")[0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)
            self.delay=conf['world']['environment']['delay']
            self.weather_change=conf['world']['environment']['change']

    def get_time(self):
        return self.clock.get_time()

    def set_time(self, string):
        self.clock.set_time(string)
        date = time.localtime(self.clock.get_time_seconds())
        if ((date.tm_mon>=3 and date.tm_mday>=20)or(date.tm_mon<=6 and date.tm_mday<21)):#spring
            self.weather.setSeason('spring')
        elif ((date.tm_mon>=6 and date.tm_mday>=21)or(date.tm_mon<=9 and date.tm_mday<22)):#summer
            self.weather.setSeason('summer')
        elif ((date.tm_mon>=9 and date.tm_mday>=22)or(date.tm_mon<=12 and date.tm_mday<21)):#autumn
            self.weather.setSeason('autumn')
        elif ((date.tm_mon>=12 and date.tm_mday>=21)or(date.tm_mon<=3 and date.tm_mday<20)):#winter
            self.weather.setSeason('winter')

    def get_weather(self):
        return self.weather.get_weather()

    def set_weather(self, string):
        self.weather.set_weather(string)

    def get_season(self):
        return self.weather.get_season()

    def start(self):
        self.start=True
        while (self.start == True):
            time.sleep(self.delay)
            date = time.localtime(self.clock.get_time_seconds())
            if ((date.tm_mon>=3 and date.tm_mday>=20)or(date.tm_mon<=6 and date.tm_mday<21)):#spring
               self.weather.setSeason('spring')
            elif ((date.tm_mon>=6 and date.tm_mday>=21)or(date.tm_mon<=9 and date.tm_mday<22)):#summer
                self.weather.setSeason('summer')
            elif ((date.tm_mon>=9 and date.tm_mday>=22)or(date.tm_mon<=12 and date.tm_mday<21)):#autumn
                self.weather.setSeason('autumn')
            elif ((date.tm_mon>=12 and date.tm_mday>=21)or(date.tm_mon<=3 and date.tm_mday<20)):#winter
                self.weather.setSeason('winter')
            y=random.randint(0,100)
            if (y<self.weather_change):
                x=random.randint(0,100)
                if (self.weather.get_season().lower()=='summer'):
                    if (x < 20):
                        self.weather.set_weather('rain')
                    elif (x < 50):
                        self.weather.set_weather('cloudy')
                    elif (x >= 50):
                        self.weather.set_weather('sunny')
                elif (self.weather.get_season().lower()=='autumn'):
                    if (x < 5):
                        self.weather.set_weather('snow')
                    elif (x < 50):
                        self.weather.set_weather('rain')
                    elif (x < 90):
                        self.weather.set_weather('cloudy')
                    elif (x >= 90):
                        self.weather.set_weather('sunny')
                elif (self.weather.get_season().lower()=='winter'):
                    if (x < 40):
                        self.weather.set_weather('snow')
                    elif (x < 50):
                        self.weather.set_weather('rain')
                    elif (x < 90):
                        self.weather.set_weather('cloudy')
                    elif (x >= 90):
                        self.weather.set_weather('sunny')
                elif (self.weather.get_season().lower()=='spring'):
                    if (x < 5):
                        self.weather.set_weather('snow')
                    elif (x < 50):
                        self.weather.set_weather('rain')
                    elif (x < 90):
                        self.weather.set_weather('cloudy')
                    elif (x >= 90):
                        self.weather.set_weather('sunny')
            self.clock.set_time_seconds(self.clock.get_time_seconds()+3600)

    def stop(self):
        self.start=False

    def get_daylight(self):
        return self.clock.get_daylight()