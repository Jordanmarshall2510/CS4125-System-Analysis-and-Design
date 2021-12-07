#Coded by Jakub Pazej - 18260179 [Add yourself here if you did any meaningful work on this class]
import json
import os
import random
from server.world.seasons import Seasons

class Weather:
    """Static weather class made to generate a weather for the simulation given a time"""
    weather='' #Sunny, Cloudy, Rain, Snow, Fog, Tornado, Sandstorm, Snowstorm
    climate='' #Tropical, Dry Cold, Dry Hot, Temperate, Continental, Polar, Desert
    weather_change_base = 70 #Base chance for weather to change
    weather_change_rate = 1 #Rate of change for chance for weather
    counter = 0 #counter for increasing chance of weather change

    @staticmethod
    def init():
        path = os.path.dirname(os.path.realpath(__file__)).split("world")[0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)
            Weather.weather=conf['world']['weather']['weather']
            Weather.delay=conf['world']['weather']['weather']
            Weather.weather_change=conf['world']['weather']['season']

    @staticmethod
    def get_weather():
        return Weather.weather

    @staticmethod
    def set_weather(string):
        if (string.lower() == 'sunny' or 'cloudy' or 'rain' or 'snow' or 'fog' or 'tornado' or 'sandstorm' or 'snowstorm'):
            Weather.weather=string.lower()

    @staticmethod
    def get_weather_change(current_weather):
        future_weather = current_weather
        x=random.randint(0,100)
      
        if (Seasons.get_season == 'summer'):
            if (x == 2):
                future_weather = 'tornado'
            if (x < 20):
                future_weather = 'rain'
            elif (x < 25):
                future_weather = 'fog'
            elif (x < 50):
                future_weather = 'cloudy'
            elif (x >= 50):
                future_weather = 'sunny'
        elif (Seasons.get_season == 'winter'):
            if (x <= 5):
                future_weather = 'fog'
            elif (x < 40):
                future_weather = 'snow'
            elif (x < 50):
                future_weather = 'rain'
            elif (x < 90):
                future_weather = 'cloudy'
            elif (x >= 90):
                future_weather = 'sunny'
        else:
            if (x == 1):
                future_weather = 'tornado'
            if (x < 5):
                future_weather = 'snow'
            elif (x < 15):
                future_weather = 'fog'
            elif (x < 50):
                future_weather = 'rain'
            elif (x < 90):
                future_weather = 'cloudy'
            elif (x >= 90):
                future_weather = 'sunny'

        if current_weather == future_weather:
            Weather.counter += Weather.weather_change_rate
            return future_weather
        else:
            Weather.counter = 0
            return future_weather

    @staticmethod
    def update_weather(current_weather):
        Weather.set_weather(Weather.get_weather_change(current_weather))



