#Coded by Jakub Pazej - 18260179
import json
import os
import random
from ElectricityGenerator.electricitygenerator import ElectricityGenerator
from World.environment import environment
from datetime import datetime

class Solar(ElectricityGenerator):
    wattage=0
    GeneratorID = 0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityGenerator")[0] + "config.json"
        with open(path) as json_file:
            conf = json.load(json_file)
            self.wattage=conf["electricityGenerator"]["solar"]["output"]

    def setGeneratorID(self, newID):
            self.GeneratorID = newID

    def update(self, date):
        now = date.now()
        current_time = now.strftime("%H")
        if(current_time<6 or current_time>20):
            return 0
        elif(current_time<12):
            a=random.randint(1,10)
            b=random.randint(1,3)
            return (self.wattage+a)+(b*Clock.getTimeHours())
        elif(current_time>12):
            a=random.randint(1,10)
            b=random.randint(1,3)
            return (self.wattage+a)+(b*(24-Clock.getTimeHours()))

    def getElectricityGenerated(self):
        return self.update()

    def generateGenerator(numberOfGenerators):
        generatedArray = []
        for x in range(numberOfGenerators):
            generator = Solar()
            generator.setGeneratorID(x + 1)
            houseData.append(generator)
        return generatedArray