# Coded by Eoin McDonough - 18241646




# TODO:
#   Distance Calculator
#   Energy output based on distance and vehicle power needs
#   Streetlights output day/night   1/2     DONE
#   Traffic lights output           1/6     DONE
#   Reduce power output of road in cold weather
#   Streetlights power output calculator is currently one hour, must make daily add up all hours in the night
#
#   put global constants in class and use self. / House. to access examples (vehicles.py: lines{28, 36, 66})
#	
#	***Extend electricityUsers and import required functions (update & getElectricityUsed)***
import random
import json
import os
# from World.Clock import Clock

path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityUser")[0] + "config.json"

with open(path) as json_file:
    conf = json.load(json_file)


AVERAGE_ELECTRICITY_USAGE = conf["electricityUser"]["infrastructure"]["averageElectricityUsage"]
STREET_LIGHT_USAGE = conf["electricityUser"]["infrastructure"]["streetLightUsage"]
TRAFFIC_LIGHT_USAGE= random.randrange(90, 160, 1)/100

class Infrastructure():
    def __init__(self, infrastructureID):
        self.infrastructureID = infrastructureID
        self.hasTrafficLight = self.setTrafficLight
        self.hasStreetLight = self.setStreetLight
        self.sumElectricitityUsage

    def setinfrastructureID(self, newID):
        self.infrastructureID = newID

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
            # Clock.getTimeOnly()
            dailyAverageUsage += STREET_LIGHT_USAGE

    def toString(self):
        return  "ID:" + self.infrastructureID + "\t\t\tTotal Electricity Usage: " + str(self.totalElectricityUsage) + "kWh" + "\t\t\tStreetLight?: " + str(self.hasStreetLight) + "\t\t\tTrafficLight?: " + str(self.hasTrafficLight)

def generateInfrastructureData(numberOfInfrastructure):    # NOTE: Will be dependent on number of houses in future
    infrastructureData = []
    infrastructureCounter = 0

    for i in range(numberOfInfrastructure):
        infrastructure = infrastructure("R" + str(infrastructureCounter))
        infrastructureData.append(infrastructure)
        infrastructureCounter += 1
    
    return infrastructureData

def sumElectricitityUsage():
    electricityUsageTolerance = 10
    dailyAverageUsage = random.randint(AVERAGE_ELECTRICITY_USAGE, AVERAGE_ELECTRICITY_USAGE + electricityUsageTolerance)/4 
    return dailyAverageUsage
  
infrastructureArray = generateInfrastructureData(10)
for i in infrastructureArray:
    print(i.toString())

    
