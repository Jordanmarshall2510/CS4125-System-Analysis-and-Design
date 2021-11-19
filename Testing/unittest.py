import unittest

# import buildings

class TestMethods(unittest.TestCase):

    # def checkIfHouse(self):
    #     house = houses.House(100000,"Test",50,5)
    #     self.assertEqual(str(house.houseValue) + "," + house.homeownerName + "," + str(house.totalElectricityUsage) + "," + str(house.numberOfOccupants), "100000,Test,50,5")

    def test(self): 
        self.assertEqual("Test", "Test")

if __name__ == '__main__':
    unittest.main()