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