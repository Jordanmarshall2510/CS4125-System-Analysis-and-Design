import unittest

# import buildings

class test_methods(unittest.TestCase):

    # def checkIfHouse(self):
    #     house = houses.House(100000,"Test",50,5)
    #     self.assertEqual(str(house.house_value) + "," + house.homeownerName + "," + str(house.total_electricity_usage) + "," + str(house.number_of_occupants), "100000,Test,50,5")

    def test(self): 
        self.assertEqual("Test", "Test")

if __name__ == '__main__':
    unittest.main()