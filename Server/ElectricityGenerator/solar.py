import json
import os
import random
from ElectricityGenerator.electricitygenerator import ElectricityGenerator
from World import environment

# FIXME: Why does Solar inherit clock ?
class Solar(ElectricityGenerator, clock):
    wattage=0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityGenerator")[0] + "config.json"
        with open(path) as json_file:
            conf = json.load(json_file)
            self.wattage=conf["electricityGenerator"]["solar"]["output"]

    # FIXME: update takes the date/time 
    def update(self, date):
        if(clock.getDayLight()==True):
            if(clock.getTimeHours()<12):
                a=random.randint(1,10)
                b=random.randint(1,3)
                return (self.wattage+a)+(b*clock.getTimeHours())
            elif(clock.getTimeHours()>12):
                a=random.randint(1,10)
                b=random.randint(1,3)
                return (self.wattage+a)+(b*(24-clock.getTimeHours()))
        elif(clock.getDayLight()==False):
            return 0

    def getElectricityGenerated(self):
        print("Here electricityGenerator method is defined")

    def generateGenerator(numberOfGenertors):
        print("Return array here")