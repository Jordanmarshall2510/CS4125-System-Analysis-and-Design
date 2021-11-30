import unittest

from server.electricity_user.businesses import Business
from server.electricity_user.houses import House
from server.electricity_user.infrastrucure import Infrastructure
from server.electricity_user.vehicles import Vehicle
from server.electricity_generator.distribution import Distribution
from server.electricity_generator.solar import Solar
from server.electricity_generator.wind import Wind
from server.database import Database
from server.world.weather import Weather

class test_methods(unittest.TestCase):

    '''
    houses.py Unit Tests
    '''

    def test_house_generation(self):
        data = House.generate_users(100)
        self.assertEqual(len(data), 100)

    def test_house_id(self):
        data = House.generate_users(1)
        self.assertIs(type(data[0].home_id), int)
    
    def test_house_number_of_occupants(self):
        data = House.generate_users(100)
        for x in data:
            self.assertTrue(1 <= x.number_of_occupants <= 10)

    def test_house_age_of_house(self):
        data = House.generate_users(100)
        for x in data:
            self.assertTrue(1 <= x.age_of_house <= 30)

    def test_house_value(self):
        data = House.generate_users(100)
        for x in data:
            self.assertTrue(50000 <= x.house_value)

    def test_house_electricity_usage(self):
        data = House.generate_users(100)
        for x in data:
            self.assertTrue(0 <= x.total_electricity_usage)

    '''
    businesses.py Unit Tests
    '''

    def test_business_generation(self):
        data = Business.generate_users(100)
        self.assertEqual(len(data), 100)

    def test_business_id(self):
        data = Business.generate_users(1)
        self.assertIs(type(data[0].business_id), str)

    def test_business_number_of_occupants(self):
        data = Business.generate_users(100)
        for x in data:
            self.assertTrue(1 <= x.number_of_occupants <= 100)

    def test_business_property_value(self):
        data = Business.generate_users(100)
        for x in data:
            self.assertTrue(0 <= x.property_value)

    def test_business_property_size(self):
        data = Business.generate_users(100)
        for x in data:
            self.assertTrue(0 <= x.property_size)
    
    def test_business_electricity_usage(self):
        data = Business.generate_users(100)
        for x in data:
            self.assertTrue(0 <= x.total_electricity_usage)

    '''
    infrastructure.py Unit Test
    '''

    def test_infrastructure_generation(self):
        data = Infrastructure.generate_users(100)
        self.assertEqual(len(data), 100)

    def test_infrastructure_id(self):
        data = Infrastructure.generate_users(1)
        self.assertIs(type(data[0].infrastructure_id), str)

    '''
    vehicles.py Unit Tests
    '''

    def test_vehicle_generation(self):
        data = Vehicle.generate_users(100)
        self.assertEqual(len(data), 100)

    def test_vehicle_id(self):
        data = Vehicle.generate_users(1)
        self.assertIs(type(data[0].vehicle_id), str) 

    def test_vehicle_number_of_passengers(self):
        data = Vehicle.generate_users(100)
        for x in data:
            self.assertTrue(0 <= x.number_of_new_passengers)

    '''
    database.py Unit Tests
    '''

    def test_database_connection(self):
        db = Database()
        self.assertTrue(db)
        del db

    '''
    distribution.py Unit Tests
    '''

    distribution = Distribution()

    '''
    solar.py Unit Tests
    '''

    def test_solar_generation(self):
        data = Solar.generate_generators(100)
        self.assertEqual(len(data), 100)

    def test_solar_id(self):
        data = Solar.generate_generators(1)
        self.assertIs(type(data[0].generator_id), int)

    def test_solar_wattage(self):
        data = Solar.generate_generators(100)
        for x in data:
            self.assertTrue(0 <= x.wattage)

    '''
    wind.py Unit Tests
    '''
    
    def test_wind_generation(self):
        data = Wind.generate_generators(100)
        self.assertEqual(len(data), 100)

    def test_wind_id(self):
        data = Wind.generate_generators(1)
        self.assertIs(type(data[0].generator_id), int)

    def test_wind_wattage(self):
        data = Wind.generate_generators(100)
        for x in data:
            self.assertTrue(0 <= x.wattage)

    '''
    weather.py Unit Tests
    '''

    weather = Weather()


if __name__ == '__main__':
    unittest.main()