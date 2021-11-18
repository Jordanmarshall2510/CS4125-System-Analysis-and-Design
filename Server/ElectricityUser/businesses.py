# Coded by Jordan Marshall - 18256716

# To Do:
#   
#   put global constants in class and use self. / House. to access examples (vehicles.py: lines{28, 36, 66})
#	
#	***Extend electricityUsers and import required functions (update & getElectricityUsed)***

import random
import json
import os
from ElectricityUser.electricityuser import ElectricityUser
from World.weather import Weather

class Business(ElectricityUser):
    path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityUser")[0] + "config.json"

    with open(path) as json_file:
        conf = json.load(json_file)

    # Average house value in Ireland. Units in euro.
    AVERAGE_PROPERTY_VALUE_PER_OCCUPANT= conf["electricityUser"]["businesses"]["averagePropertyValuePerOccupant"]

    # Electricity usage daily measured in kWh.
    AVERAGE_ELECTRICITY_USAGE = conf["electricityUser"]["businesses"]["averageElectricityUsage"]

    # Average square metre per occupant
    AVERAGE_SQM_PER_OCCUPANT = conf["electricityUser"]["businesses"]["averageSQMPerOccupant"]

    # Dictionary for seasons and weather
    WEATHER_DICTIONARY = {
        "sunny" : -0.1,
        "cloudy" : 0,
        "rain" :0.1,
        "snow" : 0.2,
        "summer" : -0.1,
        "autumn" : 0.1,
        "spring" : 0,
        "winter" : 0.2
    }

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

    # TODO: Implement Update and getElectricityUsed
    def update(self, date):
        totalUsage = self.totalElectricityUsage
        # Weather
        totalUsage += totalUsage*self.WEATHER_DICTIONARY[Weather.getSeasonChange(date)] + totalUsage*self.WEATHER_DICTIONARY[Weather.getWeatherChange('rain')]
        # Time
        
        # Distribution.output(totalUsage)
        return totalUsage


    def getElectricityUsed(self):
        return -1

    def generateUsers(numberOfBusinesses):
        businessData = []
        businessCounter = 0

        for x in range(numberOfBusinesses):
            numberOfOccupants = random.randint(1,100)
            business = Business("B" + str(businessCounter), Business.getRandomElectrictyUsage(numberOfOccupants), Business.getRandomPropertyValue(numberOfOccupants), Business.getRandomPropertySize(numberOfOccupants), numberOfOccupants)
            businessData.append(business)
            businessCounter += 1

        return businessData

    @staticmethod
    def getRandomPropertyValue(numberOfOccupants):
        propertyValueTolerance = 10000
        valuePerOccupant = random.randint(Business.AVERAGE_PROPERTY_VALUE_PER_OCCUPANT - propertyValueTolerance, Business.AVERAGE_PROPERTY_VALUE_PER_OCCUPANT + propertyValueTolerance)
        value = valuePerOccupant * numberOfOccupants
        return value

    @staticmethod
    def getRandomPropertySize(numberOfOccupants):
        propertySizeTolerance = 5
        valuePerOccupant = random.randint(Business.AVERAGE_SQM_PER_OCCUPANT - propertySizeTolerance, Business.AVERAGE_SQM_PER_OCCUPANT + propertySizeTolerance)
        value = valuePerOccupant * numberOfOccupants
        return value

    # Get random electricity usage based on number of occupants in a household
    @staticmethod
    def getRandomElectrictyUsage(numberOfOccupants):
        electricityUsageTolerance = 8
        dailyAverageUsage = random.randint(Business.AVERAGE_ELECTRICITY_USAGE - electricityUsageTolerance, Business.AVERAGE_ELECTRICITY_USAGE + electricityUsageTolerance)/4
        dailyAverageUsagePerHousehold = dailyAverageUsage * numberOfOccupants
        # FIXME: Clock has no attribute 'checkDayLight'
        # if Clock.checkDaylight() == False:
            # return dailyAverageUsagePerHousehold*2
        # else:
            # return dailyAverageUsagePerHousehold
        return dailyAverageUsagePerHousehold