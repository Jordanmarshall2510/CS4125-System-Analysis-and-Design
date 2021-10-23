########### Street Lights ###########
# Coded by Eoin McDonough - 18241646

import yaml

class StreetLight():
    totalElectricityUsage=0
    def __init__(self):
        with open('config.yaml', 'r') as f:
            config = yaml.load(f, Loader = yaml.FullLoader)
        self.time=config['world']['time']

    def setLightID(self, newID):
        self.sLightID = newID

    def setTotalElectricityUsage(self,newValue):
        self.totalElectricityUsage = newValue
        
    def calcElectricityUsage(self):
        if (self.time<900 or 1800<self.time): self.totalElectricityUsage = 0.08

########## roads ############
# Coded by Eoin McDonough - 18241646




# TODO:
#   Distance Calculator
#   Energy output based on distance and vehicle power needs
#   Streetlights output day/night   1/2     DONE
#   Traffic lights output           1/6     DONE
#   Reduce power output of road in cold weather
#   Streetlights power output calculator is currently one hour, must make daily add up all hours in the night

import random
from street_lights import StreetLight 
from traffic_lights import TrafficLight

AVERAGE_ELECTRICITY_USAGE = 30

class Road():
    def __init__(self, roadID, totalElectricityUsage):
        self.roadID = roadID
        self.totalElectricityUsage = totalElectricityUsage
        self.hasTrafficLight = setTrafficLight()
        self.hasStreetLight = setStreetLight()

    def setRoadID(self, newID):
        self.roadID = newID

    def setTotalElectricityUsage(self, newValue):
        self.totalElectricityUsage = newValue

    def toString(self):
        return  "ID:" + self.roadID + "\t\t\tTotal Electricity Usage: " + str(self.totalElectricityUsage) + "kWh" + "\t\t\tStreetLight?: " + str(self.hasStreetLight) + "\t\t\tTrafficLight?: " + str(self.hasTrafficLight)

def generateRoadData(numberOfRoads):    # NOTE: Will be dependent on number of houses in future
    roadData = []
    roadCounter = 0

    for i in range(numberOfRoads):
        road = Road("R" + str(roadCounter), sumElectricitityUsage(setStreetLight(), setTrafficLight()))
        roadData.append(road)
        roadCounter += 1
    
    return roadData

def sumElectricitityUsage(hasStreetLight,hasTrafficLight):
    electricityUsageTolerance = 10
    dailyAverageUsage = random.randint(AVERAGE_ELECTRICITY_USAGE, AVERAGE_ELECTRICITY_USAGE + electricityUsageTolerance)/4 
    if(hasStreetLight == True):
        sLight = StreetLight()
        sLight.calcElectricityUsage()
        dailyAverageUsage += sLight.totalElectricityUsage

    if(hasTrafficLight == True):
        tLight = TrafficLight()
        tLight.calcElectricityUsage
        dailyAverageUsage += tLight.totalElectricityUsage

    return dailyAverageUsage

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
        
roadArray = generateRoadData(10)
for i in roadArray:
    print(i.toString())

    
######### Traffic Light ###########
# Coded by Eoin McDonough - 18241646

import random

class TrafficLight():

    
    def __init__(self):
        self.totalElectricityUsage =0

    def setLightID(self, newID):
        self.tLightID = newID

    def setTotalElectricityUsage(self,newValue):
        self.totalElectricityUsage = newValue

    def calcElectricityUsage(self):
       totalElectricityUsage = random.randrange(0.090, 0.160, 1)
        