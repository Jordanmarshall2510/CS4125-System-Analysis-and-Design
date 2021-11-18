import unittest

from ElectricityUser.businesses import Business
from ElectricityUser.houses import House
from ElectricityUser.infrastrucure import Infrastructure
from ElectricityUser.vehicles import Vehicle
from ElectricityGenerator.distribution import Distribution
from ElectricityGenerator.solar import Solar
from ElectricityGenerator.wind import Wind
from database import Database
from World.weather import Weather

class TestMethods(unittest.TestCase):

    '''
    houses.py Unit Tests
    '''

    def testHouseGeneration(self): 
        data = House.generateUsers(100)
        self.assertEqual(len(data), 100)

    def testHouseID(self): 
        data = House.generateUsers(1)
        self.assertIs(type(data[0].homeID), int)
    
    def testHouseNumberOfOccupants(self): 
        data = House.generateUsers(100)
        for x in data:
            self.assertTrue(1 <= x.numberOfOccupants <= 10)

    def testHouseAgeOfHouse(self): 
        data = House.generateUsers(100)
        for x in data:
            self.assertTrue(1 <= x.ageOfHouse <= 30)

    def testHouseValue(self): 
        data = House.generateUsers(100)
        for x in data:
            self.assertTrue(50000 <= x.houseValue)

    def testHouseElectricityUsage(self): 
        data = House.generateUsers(100)
        for x in data:
            self.assertTrue(0 <= x.totalElectricityUsage)

    '''
    businesses.py Unit Tests
    '''

    def testBusinessGeneration(self): 
        data = Business.generateUsers(100)
        self.assertEqual(len(data), 100)

    def testBusinessID(self): 
        data = Business.generateUsers(1)
        self.assertIs(type(data[0].businessID), str) 

    def testBusinessNumberOfOccupants(self): 
        data = Business.generateUsers(100)
        for x in data:
            self.assertTrue(1 <= x.numberOfOccupants <= 100)

    def testBusinessPropertyValue(self): 
        data = Business.generateUsers(100)
        for x in data:
            self.assertTrue(0 <= x.propertyValue)

    def testBusinessPropertySize(self): 
        data = Business.generateUsers(100)
        for x in data:
            self.assertTrue(0 <= x.propertySize)
    
    def testBusinessElectricityUsage(self): 
        data = Business.generateUsers(100)
        for x in data:
            self.assertTrue(0 <= x.totalElectricityUsage)

    '''
    infrastructure.py Unit Test
    '''

    def testInfrastructureGeneration(self): 
        data = Infrastructure.generateUsers(100)
        self.assertEqual(len(data), 100)

    def testInfrastructureID(self): 
        data = Infrastructure.generateUsers(1)
        self.assertIs(type(data[0].infrastructureID), str)

    '''
    vehicles.py Unit Tests
    '''

    def testVehicleGeneration(self): 
        data = Vehicle.generateUsers(100)
        self.assertEqual(len(data), 100)

    def testVehicleID(self): 
        data = Vehicle.generateUsers(1)
        self.assertIs(type(data[0].id), str) 

    def testVehicleNumberOfPassengers(self): 
        data = Vehicle.generateUsers(100)
        for x in data:
            self.assertTrue(1 <= x.numberOfPassanagers)

    '''
    database.py Unit Tests
    '''

    def testDatabaseConnection(self): 
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

    def testSolarGeneration(self): 
        data = Solar.generateGenerators(100)
        self.assertEqual(len(data), 100)

    def testSolarID(self): 
        data = Solar.generateGenerators(1)
        self.assertIs(type(data[0].GeneratorID), int) 

    def testSolarWattage(self): 
        data = Solar.generateGenerators(100)
        for x in data:
            self.assertTrue(0 <= x.wattage)

    '''
    wind.py Unit Tests
    '''
    
    def testWindGeneration(self): 
        data = Wind.generateGenerators(100)
        self.assertEqual(len(data), 100)

    def testWindID(self): 
        data = Wind.generateGenerators(1)
        self.assertIs(type(data[0].GeneratorID), int) 

    def testWindWattage(self): 
        data = Wind.generateGenerators(100)
        for x in data:
            self.assertTrue(0 <= x.wattage)

    '''
    weather.py Unit Tests
    '''

    weather = Weather()


if __name__ == '__main__':
    unittest.main()