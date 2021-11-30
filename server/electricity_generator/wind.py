#Coded by Jakub Pazej - 18260179
from datetime import datetime
import json
import os
import random
from server.electricity_generator.electricitygenerator import ElectricityGenerator
from server.electricity_generator.distribution import Distribution
from server.world.weather import Weather

class Wind(ElectricityGenerator):
        
    #Initializing distribution object
    distribution = Distribution()

    wattage=0
    generator_id = 0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("electricity_generator")[0] + "config.json"
        with open(path) as json_file:
            conf = json.load(json_file)
            self.wattage=conf["electricity_generator"]["wind"]["output"]

    def set_generator_id(self, new_id):
        self.generator_id = new_id

    def update(self, date: datetime) -> int:
        a=random.uniform(20,30)
        total_generated = 0
        if(Weather.get_weather()=="rain"):
            total_generated = self.wattage+(a*2)
        elif(Weather.get_weather()=="cloudy"):
            total_generated = self.wattage+(a*1.5)
        else:
            total_generated = self.wattage+(a)
        self.distribution.input(total_generated,"kW")
        return total_generated

    def get_electricity_generated(self) -> int:
        return self.update()

    def generate_generators(number_of_generators: int) -> list:
        generated_array = []
        for x in range(number_of_generators):
            generator = Wind()
            generator.set_generator_id(x + 1)
            generated_array.append(generator)
        return generated_array

# List outside of class for importing
generate_wind_turbines = Wind.generate_generators