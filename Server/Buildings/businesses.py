# Coded by Jordan Marshall - 18256716

# To Do:
#   

import random
import time

# Average house value in Ireland. Units in €.
AVERAGE_PROPERTY_VALUE_PER_OCCUPANT= 32000

# Electricity usage daily measured in kWh.
AVERAGE_ELECTRICITY_USAGE = 50

# Average square metre per occupant
AVERAGE_SQM_PER_OCCUPANT = 18

class Business():
    def __init__(self, businessID, totalElectricityUsage, propertyValue, propertySize ,numberOfOccupants):
        self.businessID = businessID
        self.totalElectricityUsage = totalElectricityUsage
        self.propertyValue = propertyValue
        self.propertySize = propertySize
        self.numberOfOccupants = numberOfOccupants

    def setBusinessID(self, newID):
        self.businessID = newID
    
    def setTotalElectricityUsage(self, newValue):
        self.totalElectricityUsage = newValue

    def setPropertyValue(self, newValue):
        self.propertyValue = newValue
    
    def setPropertySize(self, newSize):
        self.propertySize = newSize

    def setNumberOfOccupants(self, newValue):
        self.numberOfOccupants = newValue

    def toString(self):
        return  "ID: " + str(self.businessID) + "\t\t\tTotal Electricity Usage: " + str(self.totalElectricityUsage) + "kWh" + "\t\t\tProperty Value: €" + str(self.propertyValue) + "\t\t\tProperty Size: " + str(self.propertySize) + "sqm" + "\t\t\tNumber of Occupants: " + str(self.numberOfOccupants)

def generateBusinessData(numberOfBusinesses):
    businessData = []
    businessCounter = 0

    for x in range(numberOfBusinesses):
        numberOfOccupants = random.randint(1,100)
        business = Business("B" + str(businessCounter), getRandomElectrictyUsage(numberOfOccupants), getRandomPropertyValue(numberOfOccupants), getRandomPropertySize(numberOfOccupants), numberOfOccupants)
        businessData.append(business)
        businessCounter += 1

    return businessData

def getRandomPropertyValue(numberOfOccupants):
    propertyValueTolerance = 10000
    valuePerOccupant = random.randint(AVERAGE_PROPERTY_VALUE_PER_OCCUPANT - propertyValueTolerance, AVERAGE_PROPERTY_VALUE_PER_OCCUPANT + propertyValueTolerance)
    value = valuePerOccupant * numberOfOccupants
    return value

def getRandomPropertySize(numberOfOccupants):
    propertySizeTolerance = 5
    valuePerOccupant = random.randint(AVERAGE_SQM_PER_OCCUPANT - propertySizeTolerance, AVERAGE_SQM_PER_OCCUPANT + propertySizeTolerance)
    value = valuePerOccupant * numberOfOccupants
    return value

# Get random electricity usage based on number of occupants in a household
def getRandomElectrictyUsage(numberOfOccupants):
    electricityUsageTolerance = 8
    dailyAverageUsage = random.randint(AVERAGE_ELECTRICITY_USAGE - electricityUsageTolerance, AVERAGE_ELECTRICITY_USAGE + electricityUsageTolerance)/4
    dailyAverageUsagePerHousehold = dailyAverageUsage * numberOfOccupants
    return dailyAverageUsagePerHousehold

# start = time.time()
businessArray = generateBusinessData(10)
for x in businessArray:
    print(x.toString())
# end = time.time()
# print("Elapsed:\t" + str(end - start) + "s")
