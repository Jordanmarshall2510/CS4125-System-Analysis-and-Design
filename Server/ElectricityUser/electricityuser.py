from abc import ABC, abstractmethod

class ElectricityUser:
    @abstractmethod
    def update(self, date):
        pass

    @abstractmethod
    def getElectricityUsed():
        pass