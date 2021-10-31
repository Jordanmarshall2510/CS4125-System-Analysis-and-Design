import json
import os
from Server import ElectricityGenerator
from World import clock

class Solar(ElectricityGenerator, clock):
    wattage= conf["electricityGenerator"]["solar"]["output"]

    def __init__(self):
           path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityGenerator")[0] + "config.json"
            with open(path) as json_file:
                conf = json.load(json_file)
                self.delay=conf['world']['environment']['delay']
                self.weather_change=conf['world']['environment']['change']

    def update():
        if(clock.checkDayLight()=True):
            return wattage
        else if(clock.checkDayLight()=False):
            return 0

    def getElectricityGenerated():
        print("Here electricityGenerator method is defined")