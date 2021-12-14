# Coded by Marcin Sek 18254187 [Add yourself here if you did any meaningful work on this class]
from abc import abstractmethod
from datetime import datetime

class ElectricityUser:
	"""ElectricityUser interface used in the creation of ElectricityUser classes"""
	@abstractmethod
	def update(self, date: datetime) -> int:
		'''Method to update the electricity usage of a specific user'''
		pass

	@staticmethod
	@abstractmethod
	def generate_users(count: int) -> list:
		'''Static method to generate a specific amount of the user type'''
		pass