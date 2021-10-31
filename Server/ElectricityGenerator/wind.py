import json
import os
import random
from Server import ElectricityGenerator
from World import environment

class Solar(ElectricityGenerator, weather):
    wattage= conf["electricityGenerator"]["wind"]["output"]

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityGenerator")[0] + "config.json"
        with open(path) as json_file:
            conf = json.load(json_file)
            self.delay=conf['world']['environment']['delay']
            self.weather_change=conf['world']['environment']['change']

    def update(self):
        a=random.randint(1,10)
        return wattage+(a*1000)

    def getElectricityGenerated(self):
        print("Here electricityGenerator method is defined")