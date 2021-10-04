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
        