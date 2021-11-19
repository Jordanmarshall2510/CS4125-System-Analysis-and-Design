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
#	***Extend electricity_users and import required functions (update & ger_electricity_used)***
import random
import json
import os

from ElectricityUser.electricityuser import ElectricityUser

class Infrastructure(electricity_user):
    average_electricity_usage = 0
    street_light_usage = 0
    traffic_light_usage = random.randrange(900, 1600, 1)/10

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

    def to_string(self):
        return  "ID:" + self.infrastructure_id + "\t\t\tTotal Electricity Usage: " + str(self.total_electricity_usage) + "kWh" + "\t\t\tStreetLight?: " + str(self.has_street_light) + "\t\t\tTrafficLight?: " + str(self.has_traffic_light)

    # TODO: implement update and ger_electricity_used
    def update(self, date): 
        return -1


    def ger_electricity_used(self):
        self.sum_electricity_usage()
        return self.total_electricity_usage

        
    def generate_users(number_of_infrastructure):    # NOTE: Will be dependent on number of houses in future
        infrastructure_data = []
        infrastructure_counter = 0

        for i in range(number_of_infrastructure):
            infrastructure = Infrastructure("R" + str(infrastructure_counter))
            infrastructure.sum_electricity_usage()
            infrastructure_data.append(infrastructure)
            infrastructure_counter += 1
        
        return infrastructure_data
    
