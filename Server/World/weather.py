# Coded by Jakub Pazej - 18260179
import json
import os
import random

# TODO: Given a date and time it should provide a weather forecast


class Weather:
    weather = ''  # Sunny, Cloudy, Rain, Snow, Fog, Tornado, Sandstorm, Snowstorm
    season = ''  # Summer, Autumn, Winter, Spring, Dry, Wet, Desert Summer, Polar Winter
    climate = ''  # Tropical, Dry Cold, Dry Hot, Temperate, Continental, Polar, Desert
    weather_change_base = 70  # Base chance for weather to change
    weather_change_rate = 1  # Rate of change for chance for weather
    counter = 0  # counter for increasing chance of weather change

    @staticmethod
    def init():
        path = os.path.dirname(os.path.realpath(__file__)).split("World")[
            0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)
            Weather.weather = conf['world']['weather']['weather']
            Weather.season = conf['world']['weather']['season']
            Weather.delay = conf['world']['weather']['weather']
            Weather.weather_change = conf['world']['weather']['season']

    @staticmethod
    def get_weather():
        return Weather.weather

    @staticmethod
    def set_weather(string):
        if (string.lower() == 'sunny' or 'cloudy' or 'rain' or 'snow' or 'fog' or 'tornado' or 'sandstorm' or 'snowstorm'):
            Weather.weather = string.lower()

    @staticmethod
    def get_season():
        return Weather.season

    @staticmethod
    def set_season(string):
        if (string.lower() == 'summer' or 'autumn' or 'winter' or 'spring' or 'dry' or 'wet' or 'desert_summer' or 'polar_winter'):
            Weather.season = string.lower()

    @staticmethod
    def get_season_change(date):

        if 3 <= int(date.strftime("%m")) <= 6:  # spring
            if 3 == int(date.strftime("%m")) and int(date.strftime("%d")) < 20:
                return 'winter'
            elif 6 == int(date.strftime("%m")) and int(date.strftime("%d")) > 20:
                return 'summer'
            else:
                return 'spring'
        elif 6 <= int(date.strftime("%m")) <= 9:  # summer
            if 9 == int(date.strftime("%m")) and int(date.strftime("%d")) > 21:
                return 'autumn'
            else:
                return 'summer'
        elif 9 <= int(date.strftime("%m")) <= 12:  # autumn
            if 12 == int(date.strftime("%m")) and int(date.strftime("%d")) > 20:
                return 'winter'
            else:
                return 'autumn'
        else:  # winter
            return 'winter'

    @staticmethod
    def get_weather_change(current_weather):
        future_weather = current_weather
        x = random.randint(0, 100)

        if (Weather.get_season == 'summer'):
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
        elif (Weather.get_season == 'winter'):
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
    def update_weather(current_weather, date):
        Weather.set_weather(Weather.get_weather_change(current_weather))
        Weather.set_season(Weather.get_season_change(date))
