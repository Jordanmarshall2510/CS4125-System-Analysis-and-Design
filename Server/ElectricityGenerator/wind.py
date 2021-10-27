import json
from Server import ElectricityGenerator

with open("config.json") as json_file:
    conf = json.load(json_file)

# Comment 1
TEST_1= conf["electricityGenerator"]["wind"]["test1"]

# Comment 2
TEST_2 = conf["electricityGenerator"]["wind"]["test2"]

# Comment 3
TEST_3 = conf["electricityGenerator"]["wind"]["test3"]

class Wind(ElectricityGenerator):
    def update(date):
        print("Here electricityGenerator method is definied")

    def getElectricityGenerated():
        print("Here electricityGenerator method is defined")