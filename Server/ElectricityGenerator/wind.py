#Coded by Jakub Pazej - 18260179
import json
import os
import random
from electricity_generator.electricity_generator import electricity_generator
from World.weather import Weather

class Wind(electricity_generator):
    wattage=0
    generator_id = 0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("electricity_generator")[0] + "config.json"
        with open(path) as json_file:
            conf = json.load(json_file)
            self.wattage=conf["electricity_generator"]["wind"]["output"]

    def set_generator_id(self, new_id):
        self.generator_id = new_id

    def update(self, date):
        a=random.uniform(20,30)
        if(Weather.get_weather()=="rain"):
            return self.wattage+(a*2)
        elif(Weather.get_weather()=="cloudy"):
            return self.wattage+(a*1.5)
        else:
            return self.wattage+(a)

    def get_electricity_generated(self):
        return self.update()

    def generateGenerators(number_of_generators):
        generated_array = []
        for x in range(number_of_generators):
            generator = Wind()
            generator.set_generator_id(x + 1)
            generated_array.append(generator)
        return generatedArray