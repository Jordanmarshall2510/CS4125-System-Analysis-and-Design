#Coded by Jakub Pazej - 18260179
import json
import os

# TODO: Given a date and time it should provide a weather forcast

class Weather:
    weather='' #Sunny, Cloudy, Rain, Snow
    season='' #Summer, Autumn, Winter, Spring

    @staticmethod
    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("World")[0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)
            self.delay=conf['world']['weather']['weather']
            self.weather_change=conf['world']['weather']['season']

    @staticmethod
    def getWeather(self):
        return self.weather

    @staticmethod
    def setWeather(self, string):
        if (string.lower() == 'sunny' or 'cloudy' or 'rain' or 'snow'):
            self.weather=string

    @staticmethod
    def getSeason(self):
        return self.season

    @staticmethod
    def setSeason(self, string):
        if (string.lower() == 'summer' or 'autumn' or 'winter' or 'spring'):
            self.season=string