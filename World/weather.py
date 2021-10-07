#Coded by Jakub Pazej - 18260179
import yaml

class weather:
    weather='' #Sunny, Cloudy, Rain, Snow
    season='' #Summer, Autumn, Winter, Spring

    def __init__(self):
                with open('config.yaml', 'r') as f:
                    config = yaml.load(f, Loader = yaml.FullLoader)
                self.weather=config['world']['weather']['weather']
                self.season=config['world']['weather']['season']

    def getWeather(self):
        return self.weather

    def setWeather(self, string):
        if (string.lower() == 'sunny' or 'cloudy' or 'rain' or 'snow'):
            self.weather=string

    def getSeason(self):
        return self.season

    def setSeason(self, string):
        if (string.lower() == 'summer' or 'autumn' or 'winter' or 'spring'):
            self.season=string