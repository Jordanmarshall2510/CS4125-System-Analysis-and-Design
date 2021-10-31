#Coded by Jakub Pazej - 18260179
import json
import os

# TODO:
#   The distribution class should hold all the electricityGenerator instances
#   When the update function triggers the class should call the updates on its genetors
#   and retrive the amount of power using getElectricityGenerated. This power will later
#   be taken by ElectricityUsers

class distribution:
    distribution_size=0 #values read and set in init
    distribution_value=0

    def __init__(self):

        path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityUser")[0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)

        self.distribution_size=conf["electricityGenerator"]["distribution"]["distributionSize"]
        self.distribution_value=conf["electricityGenerator"]["distribution"]["distributionValue"]

    def getValue(self):
        return self.distribution_value

    def getSize(self):
        return self.distribution_size

    def setValue(self, value):
        self.distribution_value = value

    def setSize(self, value):
        self.distribution_size = value
        if (self.distribution_value > self.distribution_size): self.distribution_value = self.distribution_size

    def input(self, value, unit):
        if (unit.lower() == 'watt' or 'watts'):
                self.distribution_value += value/1000000000
                if (self.distribution_value > self.distribution_size): self.distribution_value = self.distribution_size
        elif (unit.lower() == 'kilowatt' or 'kilowatts' or 'kw'):
                self.distribution_value += value/1000000
                if (self.distribution_value > self.distribution_size): self.distribution_value = self.distribution_size
        elif (unit.lower() == 'megawatt' or 'megawatts' or 'mw'):
                self.distribution_value += value/1000
                if (self.distribution_value > self.distribution_size): self.distribution_value = self.distribution_size
        elif (unit.lower() == 'gigawatt' or 'gigawatts' or 'gw'):
                self.distribution_value += value
                if (self.distribution_value > self.distribution_size): self.distribution_value = self.distribution_size
        else:
            print('wrong unit input!!!')

    def output(self, value, unit):
        if (unit.lower() == 'watt' or 'watts'):
                if (self.distribution_value - value/1000000000 < 0):
                    return False
                else:
                    self.distribution_value -= value/1000000000
                    return True
        elif (unit.lower() == 'kilowatt' or 'kilowatts' or 'kw'):
                if (self.distribution_value - value/1000000 < 0):
                    return False
                else:
                    self.distribution_value -= value/1000000
                    return True
        elif (unit.lower() == 'megawatt' or 'megawatts' or 'mw'):
                if (self.distribution_value - value/1000 < 0):
                    return False
                else:
                    self.distribution_value -= value/1000
                    return True
        elif (unit.lower() == 'gigawatt' or 'gigawatts' or 'gw'):
                if (self.distribution_value - value < 0):
                    return False
                else:
                    self.distribution_value -= value
                    return True
        else:
            print('wrong unit input!!!')