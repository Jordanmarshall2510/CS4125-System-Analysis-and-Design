import json
import os
import random
from ElectricityGenerator.electricitygenerator import ElectricityGenerator
from World import environment

# FIXME: why does solar inherit weather ?
class Wind(ElectricityGenerator, weather):
    wattage=0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityGenerator")[0] + "config.json"
        with open(path) as json_file:
            conf = json.load(json_file)
            self.wattage=conf["electricityGenerator"]["wind"]["output"]

    # TODO: implement update, getElectricityGenenerated and generateGenerators
    def update(self):
        a=random.randint(1,10)
        return self.wattage+(a*1000)

    def getElectricityGenerated(self):
        print("Here electricityGenerator method is defined")

    def generateGenerators(numberOfGenertors):
        print("return array here")