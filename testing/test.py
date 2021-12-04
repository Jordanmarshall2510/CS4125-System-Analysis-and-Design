import unittest

from server.electricity_user.businesses import Business
from server.electricity_user.houses import House
from server.electricity_user.infrastrucure import Infrastructure
from server.electricity_user.vehicles import Vehicle
from server.electricity_generator.distribution import Distribution
from server.electricity_generator.solar import Solar
from server.electricity_generator.wind import Wind
from server.world.weather import Weather
import server.database

from client.grapher import Grapher
import client.database
from client import app

class test_methods(unittest.TestCase):

    '''
    database.py (Client) Unit Tests
    '''
    # Tests database creation on clientside.
    def test_database(self):
        db = client.database.Database()
        self.assertTrue(db)
        del db

    '''
    houses.py Unit Tests
    '''

    # Tests generation of house objects
    def test_house_generation(self):
        data = House.generate_users(100)
        self.assertEqual(len(data), 100)

    # Tests on house ID type
    def test_house_id(self):
        data = House.generate_users(1)
        self.assertIs(type(data[0].home_id), int)
    
    # Tests number of occupants in house
    def test_house_number_of_occupants(self):
        data = House.generate_users(100)
        for x in data:
            self.assertTrue(1 <= x.number_of_occupants <= 10)

    # Test age of house
    def test_house_age_of_house(self):
        data = House.generate_users(100)
        for x in data:
            self.assertTrue(1 <= x.age_of_house <= 30)

    # Test house value
    def test_house_value(self):
        data = House.generate_users(100)
        for x in data:
            self.assertTrue(50000 <= x.house_value)

    # Tests electricity usage of a house
    def test_house_electricity_usage(self):
        data = House.generate_users(100)
        for x in data:
            self.assertTrue(0 <= x.total_electricity_usage)

    '''
    businesses.py Unit Tests
    '''

    # Tests generation of business objects
    def test_business_generation(self):
        data = Business.generate_users(100)
        self.assertEqual(len(data), 100)

    # Tests on business ID type
    def test_business_id(self):
        data = Business.generate_users(1)
        self.assertIs(type(data[0].business_id), str)
    
    # Tests number of occupants in business
    def test_business_number_of_occupants(self):
        data = Business.generate_users(100)
        for x in data:
            self.assertTrue(1 <= x.number_of_occupants <= 100)

    # Tests property value of business
    def test_business_property_value(self):
        data = Business.generate_users(100)
        for x in data:
            self.assertTrue(0 <= x.property_value)

    # Tests size of business
    def test_business_property_size(self):
        data = Business.generate_users(100)
        for x in data:
            self.assertTrue(0 <= x.property_size)
    
    # Tests electricity usage of a business
    def test_business_electricity_usage(self):
        data = Business.generate_users(100)
        for x in data:
            self.assertTrue(0 <= x.total_electricity_usage)

    '''
    infrastructure.py Unit Test
    '''

    # Tests generation of infrastructure objects
    def test_infrastructure_generation(self):
        data = Infrastructure.generate_users(100)
        self.assertEqual(len(data), 100)

    # Tests on infrastructure ID type
    def test_infrastructure_id(self):
        data = Infrastructure.generate_users(1)
        self.assertIs(type(data[0].infrastructure_id), str)

    '''
    vehicles.py Unit Tests
    '''
    # Tests generation of vehicle objects
    def test_vehicle_generation(self):
        data = Vehicle.generate_users(100)
        self.assertEqual(len(data), 100)

    # Tests on vehicle ID type
    def test_vehicle_id(self):
        data = Vehicle.generate_users(1)
        self.assertIs(type(data[0].vehicle_id), str) 

    def test_vehicle_number_of_passengers(self):
        data = Vehicle.generate_users(100)
        for x in data:
            self.assertTrue(0 <= x.number_of_new_passengers)

    '''
    database.py (Server) Unit Tests
    '''

    # Tests creation of database on serverside
    def test_database(self):
        db = server.database.Database()
        self.assertTrue(db)
        del db

    '''
    solar.py Unit Tests
    '''
    
    # Tests generation of solar objects
    def test_solar_generation(self):
        data = Solar.generate_generators(100)
        self.assertEqual(len(data), 100)

    # Tests on solar ID type
    def test_solar_id(self):
        data = Solar.generate_generators(1)
        self.assertIs(type(data[0].generator_id), int)

    # Test wattage generation by solar
    def test_solar_wattage(self):
        data = Solar.generate_generators(100)
        for x in data:
            self.assertTrue(0 <= x.wattage)

    '''
    wind.py Unit Tests
    '''
    
    # Tests generation of wind objects
    def test_wind_generation(self):
        data = Wind.generate_generators(100)
        self.assertEqual(len(data), 100)

    # Tests on infrastructure ID type
    def test_wind_id(self):
        data = Wind.generate_generators(1)
        self.assertIs(type(data[0].generator_id), int)

    # Test wattage generation by wind
    def test_wind_wattage(self):
        data = Wind.generate_generators(100)
        for x in data:
            self.assertTrue(0 <= x.wattage)

    '''
    weather.py Unit Tests
    '''
    # Tests set weather function
    def test_set_weather(self):
        weather = Weather()
        weather.set_weather('RAIN')
        self.assertEqual(weather.weather,'rain')

    # Tests get weather function
    def test_get_weather(self):
        weather = Weather()
        weather.set_weather('SUNNY')
        self.assertEqual(weather.get_weather(),'sunny')

# Main function
if __name__ == '__main__':
    unittest.main()