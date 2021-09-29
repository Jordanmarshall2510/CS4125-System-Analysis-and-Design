# Coded by Jordan Marshall - 18256716

# To Do:
#   Heating

import random
import time

# Average house value in Ireland. Units in €.
AVERAGE_HOUSE_VALUE = 303000

# Electricity usage daily measured in kWh.
AVERAGE_ELECTRICITY_USAGE = 40

class House():
    def __init__(self, homeID, totalElectricityUsage, houseValue, numberOfOccupants, ageOfHouse):
        self.homeID = homeID
        self.totalElectricityUsage = totalElectricityUsage
        self.houseValue = houseValue
        self.numberOfOccupants = numberOfOccupants
        self.ageOfHouse = ageOfHouse

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
        return  "ID: " + self.homeID + "\t\t\tTotal Electricity Usage: " + str(self.totalElectricityUsage) + "kWh" + "\t\t\tHouse Value: €" + str(self.houseValue) + "\t\t\tNumber of Occupants: " + str(self.numberOfOccupants) + "\t\t\tAge of House: " + str(self.ageOfHouse)

def generateHouseData(numberOfHouses):
    houseData = []
    homeCounter = 0

    for x in range(numberOfHouses):
        numberOfOccupants = random.randint(1,10)
        ageOfHouse = random.randint(1,30)
        house = House("H" + str(homeCounter), getRandomElectrictyUsage(numberOfOccupants, ageOfHouse), getRandomHouseValue(ageOfHouse), numberOfOccupants, ageOfHouse )
        houseData.append(house)
        homeCounter += 1

    return houseData

def getRandomHouseValue(ageOfHouse):
    houseValueTolerance = 100000
    value = random.randint(AVERAGE_HOUSE_VALUE - houseValueTolerance, AVERAGE_HOUSE_VALUE + houseValueTolerance)
    if ageOfHouse < 20:
        return value
    else: 
        return value - random.randint(0, houseValueTolerance)

# Get random electricity usage based on number of occupants in a household
def getRandomElectrictyUsage(numberOfOccupants, ageOfHouse):
    electricityUsageTolerance = 10
    dailyAverageUsage = random.randint(AVERAGE_ELECTRICITY_USAGE - electricityUsageTolerance, AVERAGE_ELECTRICITY_USAGE + electricityUsageTolerance)/4
    dailyAverageUsagePerHousehold = dailyAverageUsage * numberOfOccupants
    if ageOfHouse < 20:
        return dailyAverageUsagePerHousehold
    else: 
        return dailyAverageUsagePerHousehold + random.randint(0, electricityUsageTolerance) 

# start = time.time()
houseArray = generateHouseData(10)
for x in houseArray:
    print(x.toString())
# end = time.time()
# print("Elapsed:\t" + str(end - start) + "s")
