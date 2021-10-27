# Coded by Eoin McDonough - 18241646




# TODO:
#   Distance Calculator
#   Energy output based on distance and vehicle power needs
#   Streetlights output day/night   1/2     DONE
#   Traffic lights output           1/6     DONE
#   Reduce power output of road in cold weather
#   Streetlights power output calculator is currently one hour, must make daily add up all hours in the night

import random

AVERAGE_ELECTRICITY_USAGE = 30
STREET_LIGHT_USAGE = 0.08
TRAFFIC_LIGHT_USAGE= random.randrange(90, 160, 1)/100

class Road():
    def __init__(self, roadID):
        self.roadID = roadID
        self.hasTrafficLight = self.setTrafficLight
        self.hasStreetLight = self.setStreetLight
        self.sumElectricitityUsage

    def setRoadID(self, newID):
        self.roadID = newID

    def setTotalElectricityUsage(self, newValue):
        self.totalElectricityUsage = newValue

    def setStreetLight():        
        if random.randint(0, 1) == 0:
            return True
        else:
            return False

    def setTrafficLight():
        if random.randint(0, 4) == 0:
            return True
        else:
            return False

    def sumElectricitityUsage(self):
        electricityUsageTolerance = 10
        dailyAverageUsage = random.randint(AVERAGE_ELECTRICITY_USAGE, AVERAGE_ELECTRICITY_USAGE + electricityUsageTolerance)/4 
        if self.setTrafficLight() == True:
            dailyAverageUsage += TRAFFIC_LIGHT_USAGE
        #Will be reliant on time
        if self.setStreetLight() == True:
            dailyAverageUsage += STREET_LIGHT_USAGE

    def toString(self):
        return  "ID:" + self.roadID + "\t\t\tTotal Electricity Usage: " + str(self.totalElectricityUsage) + "kWh" + "\t\t\tStreetLight?: " + str(self.hasStreetLight) + "\t\t\tTrafficLight?: " + str(self.hasTrafficLight)

def generateRoadData(numberOfRoads):    # NOTE: Will be dependent on number of houses in future
    roadData = []
    roadCounter = 0

    for i in range(numberOfRoads):
        road = Road("R" + str(roadCounter))
        roadData.append(road)
        roadCounter += 1
    
    return roadData

def sumElectricitityUsage():
    electricityUsageTolerance = 10
    dailyAverageUsage = random.randint(AVERAGE_ELECTRICITY_USAGE, AVERAGE_ELECTRICITY_USAGE + electricityUsageTolerance)/4 
    return dailyAverageUsage
  
roadArray = generateRoadData(10)
for i in roadArray:
    print(i.toString())

    
