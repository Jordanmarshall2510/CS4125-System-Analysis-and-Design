# Coded by Jordan Marshall - 18256716

# To Do:
#   
#   put global constants in class and use self. / House. to access examples (vehicles.py: lines{28, 36, 66})
#	
#	***Extend electricity_users and import required functions (update & get_electricity_used)***

from datetime import datetime
import random
import json
import os
from Server.ElectricityUser.electricityuser import ElectricityUser
from Server.ElectricityGenerator.distribution import Distribution
from Server.World.seasons import Seasons
from Server.World.weather import Weather

class Business(ElectricityUser):
    
    #Initializing distribution object
    distribution = Distribution()

    path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityUser")[0] + "config.json"

    with open(path) as json_file:
        conf = json.load(json_file)

    # Average house value in Ireland. Units in euro.
    average_property_value_per_occupant= conf["electricity_user"]["businesses"]["average_property_value_per_occupant"]

    # Electricity usage daily measured in kWh.
    average_electricity_usage = conf["electricity_user"]["businesses"]["average_electricity_usage"]

    # Average square metre per occupant
    average_sqm_per_occupant = conf["electricity_user"]["businesses"]["average_sqm_per_occupant"]

    # Dictionary for seasons and weather
    weather_dictionary = {
        "sunny" : -0.1,
        "cloudy" : 0,
        "rain" :0.1,
        "snow" : 0.2,
        "summer" : -0.25,
        "autumn" : 0.2,
        "spring" : 0,
        "winter" : 0.75,
        "fog" : 0,
        "tornado" : -1,
        "sandstorm" : 0.3,
        "snowstorm" : 0.4,
        "wet" : 0,
        "dry" : 0,
        "polar_winter" : 0.5,
        "polar" : 0.3
    }

    def __init__(self, business_id, total_electricity_usage, property_value, property_size ,number_of_occupants):
        self.business_id = business_id
        self.total_electricity_usage = total_electricity_usage
        self.property_value = property_value
        self.property_size = property_size
        self.number_of_occupants = number_of_occupants

    def set_business_id(self, new_id):
        self.business_id = new_id

    def set_total_electricity_usage(self, new_value):
        self.total_electricity_usage = new_value

    def set_property_value(self, new_value):
        self.property_value = new_value

    def set_property_size(self, newSize):
        self.property_size = newSize

    def set_number_of_occupants(self, new_value):
        self.number_of_occupants = new_value

    def to_string(self):
        return  "ID: " + str(self.business_id) + "\t\t\tTotal Electricity Usage: " + str(self.total_electricity_usage) + "kWh" + "\t\t\tProperty Value: EURO " + str(self.property_value) + "\t\t\tProperty Size: " + str(self.property_size) + "sqm" + "\t\t\tNumber of Occupants: " + str(self.number_of_occupants)

    # TODO: Implement Update and ger_electricity_used
    def update(self, date: datetime) -> int:
        total_usage = self.total_electricity_usage
        # Weather
        total_usage += random.uniform(1, total_usage*self.weather_dictionary[Seasons.get_season()] + total_usage*self.weather_dictionary[Weather.get_weather()])
        # Time
        if (not (9 < int(date.strftime("%H")) < 22)):
            total_usage = total_usage*random.uniform(0.25, 0.5)    
        self.distribution.output(total_usage,"kW")
        return total_usage

    def get_electricity_used(self) -> int:
        return -1

    def generate_users(number_of_businesses: int) -> list:
        business_data = []
        business_counter = 0

        for x in range(number_of_businesses):
            number_of_occupants = random.randint(1,100)
            business = Business("B" + str(business_counter), Business.get_random_electricity_usage(number_of_occupants), Business.get_random_property_value(number_of_occupants), Business.get_random_property_size(number_of_occupants), number_of_occupants)
            business_data.append(business)
            business_counter += 1

        return business_data

    @staticmethod
    def get_random_property_value(number_of_occupants):
        property_value_tolerance = 10000
        valuePerOccupant = random.randint(Business.average_property_value_per_occupant - property_value_tolerance, Business.average_property_value_per_occupant + property_value_tolerance)
        value = valuePerOccupant * number_of_occupants
        return value

    @staticmethod
    def get_random_property_size(number_of_occupants):
        property_sizeTolerance = 5
        valuePerOccupant = random.randint(Business.average_sqm_per_occupant - property_sizeTolerance, Business.average_sqm_per_occupant + property_sizeTolerance)
        value = valuePerOccupant * number_of_occupants
        return value

    # Get random electricity usage based on number of occupants in a household
    @staticmethod
    def get_random_electricity_usage(number_of_occupants):
        electricity_usage_tolerance = 8
        daily_average_usage = random.randint(Business.average_electricity_usage - electricity_usage_tolerance, Business.average_electricity_usage + electricity_usage_tolerance)/4
        daily_average_usage_per_household = daily_average_usage * number_of_occupants
        # FIXME: Clock has no attribute 'checkDayLight'
        # if Clock.checkDaylight() == False:
            # return daily_average_usage_per_household*2
        # else:
            # return daily_average_usage_per_household
        return daily_average_usage_per_household

# List outside of class for importing
generate_businesses = Business.generate_users