# Coded by Jordan Marshall - 18256716

# To Do:
#   Heating
#   Age of building
#   Energy usage per person per household
#   Change household name to id

import random
import time

# Average house value in Ireland. Units in €.
AVERAGE_HOUSE_VALUE = 303000

# Electricity usage daily measured in kWh.
AVERAGE_ELECTRICITY_USAGE = 40

class House():
    def __init__(self, houseValue, homeownerName, totalElectricityUsage, numberOfOccupants):
        self.houseValue = houseValue
        self.homeownerName = homeownerName
        self.totalElectricityUsage = totalElectricityUsage
        self.numberOfOccupants = numberOfOccupants

    def setHouseValue(self, newValue):
        self.houseValue = newValue

    def setHomeownerName(self, newName):
        self.homeownerName = newName
    
    def setTotalElectricityUsage(self, newValue):
        self.totalElectricityUsage = newValue
    
    def setNumberOfOccupants(self, newValue):
        self.numberOfOccupants = newValue

    def toString(self):
        return  "House Value: €" + str(self.houseValue) + "\t\t\tHomeowner Name: " + self.homeownerName + "\t\t\tTotal Electricity Usage: " + str(self.totalElectricityUsage) + "kWh" + "\t\t\tNumber of Occupants: " + str(self.numberOfOccupants)

def generateHouseData(numberOfHouses):
    houseData = []
    houseValueTolerance = 100000
    electricityUsageTolerance = 15

    houseownerName = ["Smith", "O'Connell", "Davis", "O'Brien", "Jones", "McGrath", "Foster", "O'Neill", "Healy", "Potter", "Collins", "Reid", "Price", "Buckley"]

    for x in range(numberOfHouses):
        house = House(random.randint(AVERAGE_HOUSE_VALUE - houseValueTolerance, AVERAGE_HOUSE_VALUE + houseValueTolerance), random.choice(houseownerName), random.randint(AVERAGE_ELECTRICITY_USAGE - electricityUsageTolerance, AVERAGE_ELECTRICITY_USAGE + electricityUsageTolerance), random.randint(1,10))
        houseData.append(house)
    return houseData

# start = time.time()
houseArray = generateHouseData(10)
for x in houseArray:
    print(x.toString())
# end = time.time()
# print("Elapsed:\t" + str(end - start) + "s")
