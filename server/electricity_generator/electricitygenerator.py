# Coded by Marcin Sek - 18254187 [Add yourself here if you did any meaningful work on this class]
from abc import abstractmethod
from datetime import datetime


class ElectricityGenerator:
    """ElectricityGenerator interface used in the creation of ElectricityGenerator classes"""
    @abstractmethod
    def update(self, date: datetime) -> int:
        '''Method to update the electricity generated at a specific date'''
        pass

    @staticmethod
    @abstractmethod
    def generate_generators(count: int) -> list:
        '''Static method to generate a specific type of generator'''
        pass
