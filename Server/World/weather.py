#Coded by Jakub Pazej - 18260179
import json
import os
import random

# TODO: Given a date and time it should provide a weather forcast

class Weather:
    weather='' #Sunny, Cloudy, Rain, Snow
    season='' #Summer, Autumn, Winter, Spring
    counter = 0

    # Base chance for weather to change
    WEATHER_CHANGE_BASE = 70

    # Rate of change for chance for weather
    WEATHER_CHANGE_RATE = 1

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

    @staticmethod
    def getSeasonChange(date):
        if 3 <= int(date.strftime("%m")) <= 6 :#spring
            if 3 == int(date.strftime("%m")) and int(date.strftime("%d")) < 20:
                 return 'winter'
            elif 6 == int(date.strftime("%m")) and int(date.strftime("%d")) > 20:
                return 'summer'
            else:
                 return 'spring'
        elif 6 <= int(date.strftime("%m")) <= 9 :#summer
            if 9 == int(date.strftime("%m")) and int(date.strftime("%d")) > 21:
                 return 'autumn'
            else:
                return 'summer'
        elif 9 <= int(date.strftime("%m")) <= 12 :#autumn
            if 12 == int(date.strftime("%m")) and int(date.strftime("%d")) > 20:
                 return 'winter'
            else:#winter
                 return 'autumn'
        else:#winter
            return 'winter'

    @staticmethod
    def getWeatherChange(cWeather):
        fWeather = cWeather
        if random.randint(Weather.counter,100) < Weather.WEATHER_CHANGE_BASE:
            Weather.counter += Weather.WEATHER_CHANGE_RATE
            return cWeather  
        else:
            x=random.randint(0,100)
            if (Weather.getSeason == 'summer'):
                if (x < 20):
                    fWeather = 'rain'
                elif (x < 50):
                    fWeather = 'cloudy'
                elif (x >= 50):
                    fWeather = 'sunny'
            elif (Weather.getSeason == 'winter'):
                if (x < 40):
                    fWeather = 'snow'
                elif (x < 50):
                    fWeather = 'rain'
                elif (x < 90):
                    fWeather = 'cloudy'
                elif (x >= 90):
                    fWeather = 'sunny'
            else:
                if (x < 5):
                    fWeather = 'snow'
                elif (x < 50):
                    fWeather = 'rain'
                elif (x < 90):
                    fWeather = 'cloudy'
                elif (x >= 90):
                    fWeather = 'sunny'
        if cWeather == fWeather:
            Weather.counter += Weather.WEATHER_CHANGE_RATE
            return fWeather
        else:
            Weather.counter = 0
            return fWeather

