from abc import ABC, abstractmethod

class ElectricityGenerator:
    @abstractmethod
    def update(self, date):
        pass

    @abstractmethod
    def getElectricityGenerated():
        pass