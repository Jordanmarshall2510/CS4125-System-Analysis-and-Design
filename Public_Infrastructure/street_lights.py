class StreetLight():
    def __init__(self,sLightID, totalElectricityUsage):
        self.sLightID =sLightID
        self.totalElectricityUsage = totalElectricityUsage

    def setLightID(self, newID):
        self.sLightID = newID

    def setTotalElectricityUsage(self,newValue):
        self.totalElectricityUsage = newValue
        