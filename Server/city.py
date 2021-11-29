from datetime import datetime
from typing import Tuple
from Server.ElectricityGenerator.distribution import Distribution
from Server.ElectricityUser.businesses import generate_businesses
from Server.ElectricityUser.houses import generate_houses
from Server.ElectricityUser.infrastrucure import generate_infrastructure
from Server.ElectricityUser.vehicles import generate_vehicles
from Server.ElectricityGenerator.solar import generate_solar_panels
from Server.ElectricityGenerator.wind import generate_wind_turbines


class City:
	"""City class representing the city being simulated"""
	distribution = Distribution()
	users = []

	def __init__(self):
		pass

	def add_users(self, users: list) -> None:
		self.users += users
		pass

	def add_generators(self, generators: list) -> None:
		self.distribution.add_generators(generators)
		pass

	def update(self, date: datetime) -> Tuple[dict, dict]:
		"""Updates the city to date given"""
		# Update distribution
		generation = self.distribution.update(date)

		# Update ElectricityUsers
		usage = {}
		for user in self.users:
			electricityUsed = user.update(date)
			if type(user).__name__ in usage:
				usage[type(user).__name__] += electricityUsed
			else:
				usage[type(user).__name__] = electricityUsed

		# Return two dict, generation and usage
		return generation, usage

class CityBuilder:
	"""City builder class used to construct the city"""
	def __init__(self):
		# Initialise the city being constructed
		self.city = City()
		pass

	def construct_businesses(self, number_of_businesses: int) -> None:
		"""Constructs buisness for the city
		Arguments: number_of_businesses -- Number of buisnesses to be constructed
		"""
		self.city.add_users(generate_businesses(number_of_businesses))
		pass

	def construct_houses(self, number_of_houses: int) -> None:
		"""Constructs houses for the city
		Arguments: number_of_houses -- Number of houses to be constructed
		"""
		self.city.add_users(generate_houses(number_of_houses))
		pass

	def construct_infrastructure(self, size_of_infrastructure: int) -> None:
		"""Constructs infrastructure for the city
		Arguments: size_of_infrastructure -- Size of infrastructure to be constructed
		"""
		self.city.add_users(generate_infrastructure(size_of_infrastructure))
		pass

	def construct_vehicles(self, number_of_vehicles: int) -> None:
		"""Constructs vehicles for the city
		Arguments: number_of_vehicles -- Number of vehicles to be constructed
		"""
		self.city.add_users(generate_vehicles(number_of_vehicles))
		pass

	def construct_wind_turbines(self, number_of_wind_turbines: int) -> None:
		"""Constructs wind turbines for the city
		Arguments: number_of_wind_turbines -- Number of wind turbines to be constructed
		"""
		self.city.add_generators(generate_wind_turbines(number_of_wind_turbines))
		pass

	def construct_solar_panels(self, number_of_solar_panels: int) -> None:
		"""Constructs solar panels for the city
		Arguments: number_of_solar_panels -- Number of solar panels to be constructed
		"""
		self.city.add_generators(generate_solar_panels(number_of_solar_panels))
		pass

	def build(self) -> City:
		"""Returns the completed city"""
		return self.city
