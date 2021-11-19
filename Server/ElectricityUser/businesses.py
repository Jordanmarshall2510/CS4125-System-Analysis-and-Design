# Coded by Jordan Marshall - 18256716

# To Do:
#   
#   put global constants in class and use self. / House. to access examples (vehicles.py: lines{28, 36, 66})
#	
#	***Extend electricity_users and import required functions (update & ger_electricity_used)***

import random
import json
import os
from electricity_user.electricity_user import electricity_user
from World.weather import Weather

class Business(electricity_user):
    path = os.path.dirname(os.path.realpath(__file__)).split("electricity_user")[0] + "config.json"

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
        "summer" : -0.1,
        "autumn" : 0.1,
        "spring" : 0,
        "winter" : 0.2
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
    def update(self, date):
        total_usage = self.total_electricity_usage
        # Weather
        total_usage += total_usage*self.weather_dictionary[Weather.get_season_change(date)] + total_usage*self.weather_dictionary[Weather.get_weather_change('rain')]
        # Time
        
        # Distribution.output(total_usage)
        return total_usage


    def ger_electricity_used(self):
        return -1

    def generate_users(number_of_businesses):
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