#Coded by Jakub Pazej - 18260179
import json
import os
import random
from ElectricityGenerator.electricitygenerator import ElectricityGenerator
from datetime import datetime

class Solar(ElectricityGenerator):
    wattage=0
    generator_id = 0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityGenerator")[0] + "config.json"
        with open(path) as json_file:
            conf = json.load(json_file)
            self.wattage=conf["electricity_generator"]["solar"]["output"]

    def set_generator_id(self, new_id):
        self.generator_id = new_id

    def update(self, date):
        current_time = int(date.strftime("%H"))
        if(current_time<6 or current_time>20):
            return 0
        elif(current_time<=12):
            a=random.uniform(0,0.00014)
            b=random.uniform(0,0.0014)
            return (self.wattage+a)+(b*current_time)
        elif(current_time>12):
            a=random.uniform(0,0.00014)
            b=random.uniform(0,0.0014)
            return (self.wattage+a)+(b*(24-current_time))

    def get_electricity_generated(self):
        return self.update()

    def generate_generators(number_of_generators):
        generated_array = []
        for x in range(number_of_generators):
            generator = Solar()
            generator.set_generator_id(x + 1)
            generated_array.append(generator)
        return generated_array