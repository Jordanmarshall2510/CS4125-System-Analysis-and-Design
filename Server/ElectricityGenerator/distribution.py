#Coded by Jakub Pazej - 18260179
import json
import os

from ElectricityGenerator.solar import Solar
from ElectricityGenerator.wind import Wind

# TODO:
#   The distribution class should hold all the electricityGenerator instances
#   When the update function triggers the class should call the updates on its genetors
#   and retrive the amount of power using getElectricityGenerated. This power will later
#   be taken by ElectricityUsers

class Distribution:
    DISTRIBUTION_SIZE=0 #values read and set in init
    DISTRIBUTION_VALUE=0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityGenerator")[0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)

        self.arrGenerators = []
        self.arrGenerators += Solar.generateGenerators(conf["session"]["electricityGenerator"]["solar"])
        self.arrGenerators += Wind.generateGenerators(conf["session"]["electricityGenerator"]["wind"])

        self.DISTRIBUTION_SIZE=conf["electricityGenerator"]["distribution"]["distributionSize"]
        self.DISTRIBUTION_VALUE=conf["electricityGenerator"]["distribution"]["distributionValue"]


    def getValue(self):
        return self.DISTRIBUTION_VALUE

    def getSize(self):
        return self.DISTRIBUTION_SIZE

    def setValue(self, value):
        self.DISTRIBUTION_VALUE = value

    def setSize(self, value):
        self.DISTRIBUTION_SIZE = value
        if (self.DISTRIBUTION_VALUE > self.DISTRIBUTION_SIZE): self.DISTRIBUTION_VALUE = self.DISTRIBUTION_SIZE

    def input(self, value, unit):
        if (unit.lower() == 'watt' or 'watts'):
                self.DISTRIBUTION_VALUE += value/1000000000
                if (self.DISTRIBUTION_VALUE > self.DISTRIBUTION_SIZE): self.DISTRIBUTION_VALUE = self.DISTRIBUTION_SIZE
        elif (unit.lower() == 'kilowatt' or 'kilowatts' or 'kw'):
                self.DISTRIBUTION_VALUE += value/1000000
                if (self.DISTRIBUTION_VALUE > self.DISTRIBUTION_SIZE): self.DISTRIBUTION_VALUE = self.DISTRIBUTION_SIZE
        elif (unit.lower() == 'megawatt' or 'megawatts' or 'mw'):
                self.DISTRIBUTION_VALUE += value/1000
                if (self.DISTRIBUTION_VALUE > self.DISTRIBUTION_SIZE): self.DISTRIBUTION_VALUE = self.DISTRIBUTION_SIZE
        elif (unit.lower() == 'gigawatt' or 'gigawatts' or 'gw'):
                self.DISTRIBUTION_VALUE += value
                if (self.DISTRIBUTION_VALUE > self.DISTRIBUTION_SIZE): self.DISTRIBUTION_VALUE = self.DISTRIBUTION_SIZE
        else:
            print('wrong unit input!!!')

    def output(self, value, unit):
        if (unit.lower() == 'watt' or 'watts'):
                if (self.DISTRIBUTION_VALUE - value/1000000000 < 0):
                    return False
                else:
                    self.DISTRIBUTION_VALUE -= value/1000000000
                    return True
        elif (unit.lower() == 'kilowatt' or 'kilowatts' or 'kw'):
                if (self.DISTRIBUTION_VALUE - value/1000000 < 0):
                    return False
                else:
                    self.DISTRIBUTION_VALUE -= value/1000000
                    return True
        elif (unit.lower() == 'megawatt' or 'megawatts' or 'mw'):
                if (self.DISTRIBUTION_VALUE - value/1000 < 0):
                    return False
                else:
                    self.DISTRIBUTION_VALUE -= value/1000
                    return True
        elif (unit.lower() == 'gigawatt' or 'gigawatts' or 'gw'):
                if (self.DISTRIBUTION_VALUE - value < 0):
                    return False
                else:
                    self.DISTRIBUTION_VALUE -= value
                    return True
        else:
            print('wrong unit input!!!')

    def update(self, date):
        dict = {}

        # Update Generators
        for generator in self.arrGenerators:
            electricityGenerated = generator.update(date)
            if type(generator).__name__ in dict:
                dict[type(generator).__name__] += electricityGenerated
            else:
                dict[type(generator).__name__] = electricityGenerated

            # TODO: Add new Electricity to the battery

        return dict