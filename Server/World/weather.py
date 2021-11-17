#Coded by Jakub Pazej - 18260179
import json
import os

# TODO: Given a date and time it should provide a weather forcast

class Weather:
    weather='' #Sunny, Cloudy, Rain, Snow
    season='' #Summer, Autumn, Winter, Spring

    @staticmethod
    def init():
        path = os.path.dirname(os.path.realpath(__file__)).split("World")[0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)
            Weather.delay=conf['world']['weather']['weather']
            Weather.weather_change=conf['world']['weather']['season']

    @staticmethod
    def getWeather():
        return Weather.weather

    @staticmethod
    def setWeather(string):
        if (string.lower() == 'sunny' or 'cloudy' or 'rain' or 'snow'):
            Weather.weather=string.lower()

    @staticmethod
    def getSeason():
        return Weather.season

    @staticmethod
    def setSeason(string):
        if (string.lower() == 'summer' or 'autumn' or 'winter' or 'spring'):
            Weather.season=string.lower()