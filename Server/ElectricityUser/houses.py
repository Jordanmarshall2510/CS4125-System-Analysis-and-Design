# Coded by Jordan Marshall - 18256716

# To Do:
#   Heating
#	
#import required functions (update & get_electricity_used)***

from datetime import datetime
import random
import json
import os

from ElectricityUser.electricityuser import ElectricityUser
from ElectricityGenerator.distribution import Distribution
from World.weather import Weather

class House(ElectricityUser):
    average_house_value = 0
    average_electricity_usage = 0

    # Dictionary for seasons and weather
    weather_dictionary = {
        "sunny" : -0.1,
        "cloudy" : 0,
        "rain" :0.1,
        "snow" : 0.2,
        "summer" : -0.05,
        "autumn" : 0.05,
        "spring" : 0.00,
        "winter" : 0.01
    }

    def __init__(self):

        path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityUser")[0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)

        # Average house value in Ireland. Units in €.
        self.average_house_value = conf["electricity_user"]["houses"]["average_house_value"]

        # Electricity usage daily measured in kWh.
        self.average_electricity_usage = conf["electricity_user"]["houses"]["average_electricity_value"]

        self.home_id = 0
        self.number_of_occupants = random.randint(1,10)
        self.age_of_house = random.randint(1,30)
        self.total_electricity_usage = self.get_random_electricity_usage(self.number_of_occupants, self.age_of_house)
        self.house_value = self.get_random_house_value(self.age_of_house)

    def set_home_id(self, new_id):
        self.home_id = new_id
    
    def set_total_electricity_usage(self, new_value):
        self.total_electricity_usage = new_value

    def set_house_value(self, new_value):
        self.house_value = new_value
    
    def set_number_of_occupants(self, new_value):
        self.number_of_occupants = new_value

    def set_age_of_house(self, new_value):
        self.age_of_house = new_value

    def to_string(self):
        return  "ID: " + str(self.home_id) + "\t\t\tTotal Electricity Usage: " + str(self.total_electricity_usage) + "kWh" + "\t\t\tHouse Value: €" + str(self.house_value) + "\t\t\tNumber of Occupants: " + str(self.number_of_occupants) + "\t\t\tAge of House: " + str(self.age_of_house)

    def get_random_house_value(self, age_of_house):
        house_value_tolerance = 100000
        value = random.randint(self.average_house_value - house_value_tolerance, self.average_house_value + house_value_tolerance)
        if age_of_house < 20:
            return value
        else: 
            return value - random.randint(0, house_value_tolerance)

    # Get random electricity usage based on number of occupants in a household
    def get_random_electricity_usage(self, number_of_occupants, age_of_house):
        electricity_usage_tolerance = 10
        daily_average_usage = random.randint(self.average_electricity_usage - electricity_usage_tolerance, self.average_electricity_usage + electricity_usage_tolerance)/4
        daily_average_usage_per_household = daily_average_usage * number_of_occupants
        if age_of_house < 20:
            return daily_average_usage_per_household
        else: 
            return daily_average_usage_per_household + random.randint(0, electricity_usage_tolerance)

    # TODO: implement update and ger_electricity_used
    def update(self, date : datetime) -> int:
        total_usage = self.total_electricity_usage
        season_value = self.weather_dictionary[Weather.get_season_change(date)]
        if season_value > 0:
            total_usage += random.randint(0, int(total_usage * season_value))
        elif season_value < 0:
            total_usage -= random.randint(0, int(total_usage * -season_value))
        return total_usage

    def get_electricity_used(self) -> int:
        return -1

    def generate_users(number_of_houses : int) -> list:
        house_data = []
        for x in range(number_of_houses):
            house = House()
            house.set_home_id(x + 1)
            house_data.append(house)

        return house_data

# List outside of class for importing
generate_houses = House.generate_users
