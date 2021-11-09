# Coded by Jordan Marshall - 18256716

# To Do:
#   Heating
#	
#	***Extend electricityUsers and import required functions (update & getElectricityUsed)***

import random
import json
import os

class House():
    AVERAGE_HOUSE_VALUE = 0
    AVERAGE_ELECTRICITY_USAGE = 0

    def __init__(self):

        path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityUser")[0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)

        # Average house value in Ireland. Units in €.
        self.AVERAGE_HOUSE_VALUE = conf["electricityUser"]["houses"]["averageHouseValue"]

        # Electricity usage daily measured in kWh.
        self.AVERAGE_ELECTRICITY_USAGE = conf["electricityUser"]["houses"]["averageElectricityValue"]

        self.homeID = 0
        self.numberOfOccupants = random.randint(1,10)
        self.ageOfHouse = random.randint(1,30)
        self.totalElectricityUsage = self.getRandomElectrictyUsage(self.numberOfOccupants, self.ageOfHouse)
        self.houseValue = self.getRandomHouseValue(self.ageOfHouse)

    def setHomeID(self, newID):
        self.homeID = newID
    
    def setTotalElectricityUsage(self, newValue):
        self.totalElectricityUsage = newValue

    def setHouseValue(self, newValue):
        self.houseValue = newValue
    
    def setNumberOfOccupants(self, newValue):
        self.numberOfOccupants = newValue

    def setAgeOfHouse(self, newValue):
        self.ageOfHouse = newValue

    def toString(self):
        return  "ID: " + str(self.homeID) + "\t\t\tTotal Electricity Usage: " + str(self.totalElectricityUsage) + "kWh" + "\t\t\tHouse Value: €" + str(self.houseValue) + "\t\t\tNumber of Occupants: " + str(self.numberOfOccupants) + "\t\t\tAge of House: " + str(self.ageOfHouse)

    def getRandomHouseValue(self, ageOfHouse):
        houseValueTolerance = 100000
        value = random.randint(self.AVERAGE_HOUSE_VALUE - houseValueTolerance, self.AVERAGE_HOUSE_VALUE + houseValueTolerance)
        if ageOfHouse < 20:
            return value
        else: 
            return value - random.randint(0, houseValueTolerance)

    # Get random electricity usage based on number of occupants in a household
    def getRandomElectrictyUsage(self, numberOfOccupants, ageOfHouse):
        electricityUsageTolerance = 10
        dailyAverageUsage = random.randint(self.AVERAGE_ELECTRICITY_USAGE - electricityUsageTolerance, self.AVERAGE_ELECTRICITY_USAGE + electricityUsageTolerance)/4
        dailyAverageUsagePerHousehold = dailyAverageUsage * numberOfOccupants
        if ageOfHouse < 20:
            return dailyAverageUsagePerHousehold
        else: 
            return dailyAverageUsagePerHousehold + random.randint(0, electricityUsageTolerance) 

def generateHouses(numberOfHouses):
    houseData = []
    for x in range(numberOfHouses):
        house = House()
        house.setHomeID(x + 1)
        houseData.append(house)

    return houseData
