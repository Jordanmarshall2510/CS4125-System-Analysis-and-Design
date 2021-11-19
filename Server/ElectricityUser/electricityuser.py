from abc import abstractmethod

class electricity_user:
    @abstractmethod
    def update(self, date):
        '''Method to update the electricity usage of a specific user'''
        pass

    @abstractmethod
    def ger_electricity_used(self):
        '''Method to get the total electricity used by the user'''
        pass

    @staticmethod
    @abstractmethod
    def generate_users(count):
        '''Static method to generate a specific amount of the user type'''
        pass