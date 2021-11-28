# Coded by Jakub Pazej - 18260179
import json
import os

# TODO:
#   The distribution class should hold all the electricity_generator instances
#   When the update function triggers the class should call the updates on its generators
#   and retrieve the amount of power using get_electricity_generated. This power will later
#   be taken by electricity_users


class Distribution:
    distribution_size = 0  # values read and set in init
    distribution_value = 0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split(
            "ElectricityGenerator")[0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)

        self.generators_array = []

        self.distribution_size = conf["electricity_generator"]["distribution"]["distribution_size"]
        self.distribution_value = conf["electricity_generator"]["distribution"]["distribution_value"]

    def add_generators(self, generators: list) -> None:
        """Method to add generators to the distribution class
        Arguments: generators -- A list of ElectricityGenerators being added
        """
        self.generators_array += generators
        pass

    def get_value(self):
        return self.distribution_value

    def get_size(self):
        return self.distribution_size

    def set_value(self, value):
        self.distribution_value = value

    def set_size(self, value):
        self.distribution_size = value
        if (self.distribution_value > self.distribution_size):
            self.distribution_value = self.distribution_size

    def input(self, value, unit):
        if (unit.lower() == 'watt' or 'watts'):
            self.distribution_value += value/1000000000
            if (self.distribution_value > self.distribution_size):
                self.distribution_value = self.distribution_size
        elif (unit.lower() == 'kilowatt' or 'kilowatts' or 'kw'):
            self.distribution_value += value/1000000
            if (self.distribution_value > self.distribution_size):
                self.distribution_value = self.distribution_size
        elif (unit.lower() == 'megawatt' or 'megawatts' or 'mw'):
            self.distribution_value += value/1000
            if (self.distribution_value > self.distribution_size):
                self.distribution_value = self.distribution_size
        elif (unit.lower() == 'gigawatt' or 'gigawatts' or 'gw'):
            self.distribution_value += value
            if (self.distribution_value > self.distribution_size):
                self.distribution_value = self.distribution_size
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

    def update(self, date):
        dict = {}

        # Update Generators
        for generator in self.generators_array:
            electricity_generated = generator.update(date)
            if type(generator).__name__ in dict:
                dict[type(generator).__name__] += electricity_generated
            else:
                dict[type(generator).__name__] = electricity_generated

            # TODO: Add new Electricity to the battery

        return dict
