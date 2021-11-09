from abc import abstractmethod

class ElectricityUser:
    @abstractmethod
    def update(self, date):
        '''Method to update the electricity usage of a specific user'''
        pass

    @abstractmethod
    def getElectricityUsed(self):
        '''Method to get the total electricity used by the user'''
        pass

    @staticmethod
    @abstractmethod
    def generateUsers(count):
        '''Static method to generate a specific amount of the user type'''
        pass