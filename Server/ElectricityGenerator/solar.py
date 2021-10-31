import json
import os
import random
from Server import ElectricityGenerator
from World import environment

class Solar(ElectricityGenerator, clock):
    wattage= conf["electricityGenerator"]["solar"]["output"]

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityGenerator")[0] + "config.json"
        with open(path) as json_file:
            conf = json.load(json_file)
            self.delay=conf['world']['environment']['delay']
            self.weather_change=conf['world']['environment']['change']

    def update(self):
        if(clock.getDayLight()==True):
            if(clock.getTimeHours()<12):
                a=random.randint(1,10)
                b=random.randint(1,3)
                return (wattage+a)+(b*clock.getTimeHours())
            else if(clock.getTimeHours()>12):
                a=random.randint(1,10)
                b=random.randint(1,3)
                return (wattage+a)+(b*(24-clock.getTimeHours())
        else if(clock.getDayLight()==False):
            return 0

    def getElectricityGenerated(self):
        print("Here electricityGenerator method is defined")