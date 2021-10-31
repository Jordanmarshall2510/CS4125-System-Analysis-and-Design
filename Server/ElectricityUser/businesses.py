# Coded by Jordan Marshall - 18256716

# To Do:
#   
#   put global constants in class and use self. / House. to access examples (vehicles.py: lines{28, 36, 66})
#	
#	***Extend electricityUsers and import required functions (update & getElectricityUsed)***

import random
import time
import json
import os
from Server.World.clock import clock
import electricityuser

class Business():
    path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityUser")[0] + "config.json"

    with open(path) as json_file:
        conf = json.load(json_file)

    # Average house value in Ireland. Units in euro.
    AVERAGE_PROPERTY_VALUE_PER_OCCUPANT= conf["electricityUser"]["businesses"]["averagePropertyValuePerOccupant"]

    # Electricity usage daily measured in kWh.
    AVERAGE_ELECTRICITY_USAGE = conf["electricityUser"]["businesses"]["averageElectricityUsage"]

    # Average square metre per occupant
    AVERAGE_SQM_PER_OCCUPANT = conf["electricityUser"]["businesses"]["averageSQMPerOccupant"]

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
        return  "ID: " + str(self.businessID) + "\t\t\tTotal Electricity Usage: " + str(self.totalElectricityUsage) + "kWh" + "\t\t\tProperty Value: EURO " + str(self.propertyValue) + "\t\t\tProperty Size: " + str(self.propertySize) + "sqm" + "\t\t\tNumber of Occupants: " + str(self.numberOfOccupants)

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
    if Clock.checkDaylight() == False:
        return dailyAverageUsagePerHousehold*2
    else:
        return dailyAverageUsagePerHousehold

# start = time.time()
# businessArray = generateBusinessData(10)
# for x in businessArray:
#     print(x.toString())
# end = time.time()
# print("Elapsed:\t" + str(end - start) + "s")