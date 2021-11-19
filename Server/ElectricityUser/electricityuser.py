from abc import abstractmethod
from datetime import datetime

class ElectricityUser:
	@abstractmethod
	def update(self, date : datetime) -> int:
		'''Method to update the electricity usage of a specific user'''
		pass

	@abstractmethod
	def ger_electricity_used(self) -> int:
		'''Method to get the total electricity used by the user'''
		pass

	@staticmethod
	@abstractmethod
	def generate_users(count : int) -> list:
		'''Static method to generate a specific amount of the user type'''
		pass