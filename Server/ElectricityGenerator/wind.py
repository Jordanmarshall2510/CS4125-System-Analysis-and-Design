#Coded by Jakub Pazej - 18260179
import json
import os
import random
from ElectricityGenerator.electricitygenerator import ElectricityGenerator
from World.weather import Weather

class Wind(ElectricityGenerator):
    wattage=0
    GeneratorID = 0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityGenerator")[0] + "config.json"
        with open(path) as json_file:
            conf = json.load(json_file)
            self.wattage=conf["electricityGenerator"]["wind"]["output"]

    def update(self, date):
        a=random.randint(1,10)
        if(Weather.getWeather()=="rain"):
            return self.wattage+(a*1200)
        elif(Weather.getWeather()=="cloudy"):
            return self.wattage+(a*1100)
        else:
            return self.wattage+(a*1000)

    def getElectricityGenerated(self):
        return self.update()

    def generateGenerators(numberOfGenerators):
        generatedArray = []
        for x in range(numberOfGenerators):
            generator = Wind()
            generator.setGeneratorID(x + 1)
            generatedArray.append(generator)
        print(generatedArray)
        return generatedArray