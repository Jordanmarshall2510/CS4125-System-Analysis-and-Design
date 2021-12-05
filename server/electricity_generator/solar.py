#Coded by Jakub Pazej - 18260179 [Add yourself here if you did any meaningful work on this class]
import json
import os
import random
from server.electricity_generator.electricitygenerator import ElectricityGenerator
from server.electricity_generator.distribution import Distribution
from datetime import datetime

class Solar(ElectricityGenerator):
    """Solar class representing a solar panel in the city"""
        
    #Initializing distribution object
    distribution = Distribution()

    wattage=0
    generator_id = 0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("electricity_generator")[0] + "config.json"
        with open(path) as json_file:
            conf = json.load(json_file)
            self.wattage=conf["electricity_generator"]["solar"]["output"]

    def set_generator_id(self, new_id):
        self.generator_id = new_id

    def update(self, date: datetime) -> int:
        current_time = int(date.strftime("%H"))
        total_generated = 0
        if(current_time<6 or current_time>20):
            total_generated = 0
        elif(current_time<=12):
            a=random.uniform(0,0.00014)
            b=random.uniform(0,0.0014)
            total_generated = (self.wattage+a)+(b*current_time)
        elif(current_time>12):
            a=random.uniform(0,0.00014)
            b=random.uniform(0,0.0014)
            total_generated = (self.wattage+a)+(b*(24-current_time))
        self.distribution.input(total_generated,"kW")
        return total_generated

    def get_electricity_generated(self) -> int:
        return self.update()

    def generate_generators(number_of_generators: int) -> list:
        generated_array = []
        for x in range(number_of_generators):
            generator = Solar()
            generator.set_generator_id(x + 1)
            generated_array.append(generator)
        return generated_array

# List outside of class for importing
generate_solar_panels = Solar.generate_generators