import json
import os
from Server import ElectricityGenerator

# TODO:
#   if the system is calculating generation hourly then update should calculate what an hour of solar power will
#   be, then this data can be retrieved with the getElectricityGenerated function

path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityGenerator")[0] + "config.json"

with open(path) as json_file:
    conf = json.load(json_file)

# Comment 1
TEST_1= conf["electricityGenerator"]["solar"]["test1"]

# Comment 2
TEST_2 = conf["electricityGenerator"]["solar"]["test2"]

# Comment 3
TEST_3 = conf["electricityGenerator"]["solar"]["test3"]

class Solar(ElectricityGenerator):
    def update(date):
        print("Here electricityGenerator method is definied")

    def getElectricityGenerated():
        print("Here electricityGenerator method is defined")