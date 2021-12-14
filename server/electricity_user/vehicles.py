# Coded by Marcin Sek - 18254187 [Add yourself here if you did any meaningful work on this class]
from datetime import datetime
import random
import json
import os

from server.electricity_user.electricityuser import ElectricityUser
from server.electricity_generator.distribution import Distribution
from server.world.weather import Weather
from server.world.seasons import Seasons

class Vehicle(ElectricityUser):
	"""Vehicle class representing vehicles in the city simulation"""

	#Initializing distribution object
	distribution = Distribution()

	# Read initialising data from json
	path = os.path.dirname(os.path.realpath(__file__)).split("electricity_user")[0] + "config.json"
	with open(path) as json_file:
		conf = json.load(json_file)

	weather_dictionary = {
        "sunny" : -0.3,
        "cloudy" : 0.1,
        "rain" :0.3,
        "snow" : 0.5,
        "summer" : -0.3,
        "autumn" : 0.2,
        "spring" : 0.00,
        "winter" : 0.6,
        "fog" : 0.3,
        "tornado" : 0.4,
        "sandstorm" : 0.5,
        "snowstorm" : 0.7,
        "wet" : 0.4,
        "dry" : 0,
        "polar_winter" : 0.5,
        "polar" : 0.3
    }
		
	# Average electric car value. Units in EURO
	average_vehicle_value= conf["electricity_user"]["vehicles"]["average_vehicle_value"]

	# Average electric car battery capacity. Units in kWh
	average_battery_capacity = conf["electricity_user"]["vehicles"]["average_battery_capacity"]

	# Average electric car range. Units in KM
	average_range = conf["electricity_user"]["vehicles"]["average_range"]

	# Average decrease in range per person. Units %
	average_new_passenger_range_cost = conf["electricity_user"]["vehicles"]["average_passenger_range_cost"]

	def __init__(self, vehicle_id, vehicle_value, battery_capacity, range, number_of_new_passengers):
		"""Intialize a vehicle object"""
		self.vehicle_id = vehicle_id
		self.vehicle_value = vehicle_value
		self.battery_capacity = battery_capacity
		self.max_range = range
		self.number_of_new_passengers = number_of_new_passengers
		self.real_range = int(self.max_range - (self.max_range * self.average_new_passenger_range_cost * self.number_of_new_passengers))

	# TODO: increase complexity of update function with relation to the following:
	# 1.) Driving in cold / snowy conditions can decrease the efficiency of the battery by up to 19% on Average
	# 	as found here: https://www.autoweek.com/news/green-cars/a31898441/study-ev-winter-range-loss-averages-19/
	# 	NOTE: Lower battery efficiency results in more energy being used to travel the same distance.
	def update(self, date: datetime) -> int:
		total_usage = self.battery_capacity
		current_time = int(date.strftime("%H"))
		total_usage += random.uniform(1, total_usage*self.weather_dictionary[Seasons.get_season()] + total_usage*self.weather_dictionary[Weather.get_weather()])
		if Seasons.get_season == 'winter':
			timetoChange = 8
			timetoEnd = 17
		else:
			timetoChange = 6
			timetoEnd = 20
		if (current_time<timetoChange or current_time>timetoEnd):
			multiplier = random.randrange(1,2)
			total_usage = total_usage*multiplier
		self.distribution.output(total_usage,"kW")
		return total_usage

	def set_vehicle_id(self, new_id: int):
		"""Change vehicle ID"""
		self.vehicle_id = new_id
	
	def set_vehicle_value(self, new_value: int):
		"""Change vehicle value"""
		self.vehicle_value = new_value

	def set_battery_capacity(self, new_capacity: int):
		"""Change vehicle battery capacity"""
		self.battery_capacity = new_capacity

	def set_vehicle_range(self, new_range: int):
		"""Change vehicle range"""
		self.max_range = new_range
	
	def set_number_of_new_passengers(self, new_new_passengers: int):
		"""Change number of occupants"""
		self.number_of_new_passengers = new_new_passengers
		self.real_range = int(self.max_range - (self.max_range * (self.average_new_passenger_range_cost * self.number_of_new_passengers)))

	def generate_users(number_of_vehicles: int) -> list:
		vehicle_data = []
		vehicle_value_tolerance = 10000
		battery_capacity_tolerance = 15
		vehicle_range_tolerance = 50

		for i in range(number_of_vehicles):
			# Generate Values
			vehicle_id = "C" + str(i)
			vehicle_value = random.randint(Vehicle.average_vehicle_value- vehicle_value_tolerance, Vehicle.average_vehicle_value+ vehicle_value_tolerance)
			battery_cap = random.randint(Vehicle.average_battery_capacity - battery_capacity_tolerance, Vehicle.average_battery_capacity + battery_capacity_tolerance)
			vehicleRange = random.randint(Vehicle.average_range - vehicle_range_tolerance, Vehicle.average_range + vehicle_range_tolerance)
			passengers = random.randint(0, 5)

			# Generate Vehicle
			vehicle = Vehicle(vehicle_id, vehicle_value, battery_cap, vehicleRange, passengers)
			vehicle_data.append(vehicle)
		return vehicle_data

	def to_string(self) -> str:
		"""Return vehicle as a string"""
		return  "Vehicle: " + self.id + "\tVehicle Value: €" + str(self.vehicle_value) + "\tTotal Battery Capacity: " + str(self.battery_capacity) + "kWh" + "\tMax vehicle range: " + str(self.max_range) + "KM" + "\tReal vehicle range: " + str(self.real_range) + "KM" + "\tNumber of passengers: " + str(self.number_of_new_passengers)

# List outside of class for importing
generate_vehicles = Vehicle.generate_users
