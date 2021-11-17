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
                 return 'autumn'
            else:#winter
                 return 'autumn'
        else:
            return 'winter'
    
    # @staticmethod
    # def update(self, date):
    #     y=random.randint(0,100)
    #     if (y<self.weather_change):
    #         x=random.randint(0,100)
    #         if (self.weather.getSeason().lower()=='summer'):
    #             if (x < 20):
    #                 self.weather.setWeather('rain')
    #             elif (x < 50):
    #                 self.weather.setWeather('cloudy')
    #             elif (x >= 50):
    #                 self.weather.setWeather('sunny')
    #         elif (self.weather.getSeason().lower()=='autumn'):
    #             if (x < 5):
    #                 self.weather.setWeather('snow')
    #             elif (x < 50):
    #                 self.weather.setWeather('rain')
    #             elif (x < 90):
    #                 self.weather.setWeather('cloudy')
    #             elif (x >= 90):
    #                 self.weather.setWeather('sunny')
    #         elif (self.weather.getSeason().lower()=='winter'):
    #             if (x < 40):
    #                 self.weather.setWeather('snow')
    #             elif (x < 50):
    #                 self.weather.setWeather('rain')
    #             elif (x < 90):
    #                 self.weather.setWeather('cloudy')
    #             elif (x >= 90):
    #                 self.weather.setWeather('sunny')
    #         elif (self.weather.getSeason().lower()=='spring'):
    #             if (x < 5):
    #                 self.weather.setWeather('snow')
    #             elif (x < 50):
    #                 self.weather.setWeather('rain')
    #             elif (x < 90):
    #                 self.weather.setWeather('cloudy')
    #             elif (x >= 90):
    #                 self.weather.setWeather('sunny')
