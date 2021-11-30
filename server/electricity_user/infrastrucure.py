# Coded by Eoin McDonough - 18241646




# TODO:
#   Distance Calculator
#   Energy output based on distance and vehicle power needs
#   Streetlights output day/night   1/2     DONE
#   Traffic lights output           1/6     DONE
#   Reduce power output of road in cold weather
#   Streetlights power output calculator is currently one hour, must make daily add up all hours in the night
#
#   put global constants in class and use self. / House. to access examples (vehicles.py: lines{28, 36, 66})
#	
#	***Extend electricity_users and import required functions (update & get_electricity_used)***
import random
import json
import os

from server.electricity_user.electricityuser import ElectricityUser
from server.electricity_generator.distribution import Distribution
from datetime import datetime
from server.world.seasons import Seasons
from server.world.weather import Weather

class Infrastructure(ElectricityUser):
       
    #Initializing distribution object
    distribution = Distribution()
    
    average_electricity_usage = 0
    street_light_usage = 0
    traffic_light_usage = random.randrange(900, 1600, 1)/10

    weather_dictionary = {
        "sunny" : -0.2,
        "cloudy" : 0.2,
        "rain" :0.3,
        "snow" : 0.4,
        "summer" : -0.2,
        "autumn" : 0.2,
        "spring" : 0,
        "winter" : 0.5,
        "fog" : 0.1,
        "tornado" : 0.2,
        "sandstorm" : 0.1,
        "snowstorm" : 0.2,
        "wet" : 0,
        "dry" : 0,
        "polar_winter" : 0.2,
        "polar" : 0.2
    }

    def __init__(self, infrastructure_id):

        path = os.path.dirname(os.path.realpath(__file__)).split("electricity_user")[0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)

        self.average_electricity_usage = conf["electricity_user"]["infrastructure"]["average_electricity_usage"]
        self.street_light_usage = conf["electricity_user"]["infrastructure"]["street_light_usage"]


        self.infrastructure_id = infrastructure_id
        self.has_traffic_light = self.set_traffic_light()
        self.has_street_light = self.set_street_light()
        self.sum_electricity_usage

    def set_infrastructure_id(self, new_id):
        self.infrastructure_id = new_id

    def set_total_electricity_usage(self, new_value):
        self.total_electricity_usage = new_value

    def set_street_light(self):
        if random.randint(0, 1) == 0:
            return True
        else:
            return False

    def set_traffic_light(self):
        if random.randint(0, 4) == 0:
            return True
        else:
            return False

    def sum_electricity_usage(self):
        electricity_usage_tolerance = 10
        daily_average_usage = random.randint(self.average_electricity_usage, self.average_electricity_usage + electricity_usage_tolerance)/4
        if self.set_traffic_light() == True:
            daily_average_usage += self.traffic_light_usage
        #Will be reliant on time
        if self.set_street_light() == True:
            # Clock.get_time_only()
            daily_average_usage += self.street_light_usage
        self.total_electricity_usage = daily_average_usage

    def sum_electricity_usage_date(self,date ):
        electricity_usage_tolerance = 10
        daily_average_usage = random.randint(self.average_electricity_usage, self.average_electricity_usage + electricity_usage_tolerance)/4
        if self.set_traffic_light() == True:
            daily_average_usage += self.traffic_light_usage
        #Will be reliant on time
        if self.set_street_light() == True:
            current_time = int(date.strftime("%H"))
            if Seasons.get_season == 'winter':
                timetoChange = 8
                timetoEnd = 17
            else:
                timetoChange = 6
                timetoEnd = 20
            if (current_time<timetoChange or current_time>timetoEnd):
                daily_average_usage += self.street_light_usage
        self.total_electricity_usage = daily_average_usage

    def to_string(self):
        return  "ID:" + self.infrastructure_id + "\t\t\tTotal Electricity Usage: " + str(self.total_electricity_usage) + "kWh" + "\t\t\tStreetLight?: " + str(self.has_street_light) + "\t\t\tTrafficLight?: " + str(self.has_traffic_light)

    # TODO: implement update and get_electricity_used
    def update(self, date: datetime) -> int: 
        self.sum_electricity_usage_date(date)
        total_usage = self.total_electricity_usage
        total_usage += random.uniform(1, total_usage*self.weather_dictionary[Seasons.get_season()] + total_usage*self.weather_dictionary[Weather.get_weather()])
        self.distribution.output(total_usage,"kW")
        return total_usage
        

    def get_electricity_used(self) -> int:
        
        return -1

        
    def generate_users(number_of_infrastructure: int) -> list:    # NOTE: Will be dependent on number of houses in future
        infrastructure_data = []
        infrastructure_counter = 0

        for i in range(number_of_infrastructure):
            infrastructure = Infrastructure("R" + str(infrastructure_counter))
            infrastructure.sum_electricity_usage()
            infrastructure_data.append(infrastructure)
            infrastructure_counter += 1
        
        return infrastructure_data

# List outside of class for importing
generate_infrastructure = Infrastructure.generate_users
