from abc import ABC, abstractmethod

class ElectricityGenerater:
    @abstractmethod
    def update(self, date):
        pass

    @abstractmethod
    def getElectricityGenerated():
        pass