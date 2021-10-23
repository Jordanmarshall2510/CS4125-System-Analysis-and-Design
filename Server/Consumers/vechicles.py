## Coded by Marcin Sek 18254187
# TODO:
#	Reduce range based on temperature
#	NOTE: Winter / cold weather can cause a decrease of up to 25%
#	Reduce battery performance overtime
#	NOTE: Battery degredation on average is 1% SOH per 6 months

# import time
import random

# Average electric car value. Units in €
AVERAGE_VEHICLE_VALUE = 45000

# Average electric car battery capacity. Units in kWh
AVERAGE_BATTERY_CAPACITY = 60

# Average electric car range. Units in KM
AVERAGE_RANGE = 300

# Average decrease in range per person. Units %
AVERAGE_PASSANGER_RANGE_COST = 0.06

class Vechicle():
	def __init__(self, id, vehicleValue, batteryCapacity, range, numberOfPassanagers):
		self.id = id
		self.vehicleValue = vehicleValue
		self.batteryCapacity = batteryCapacity
		self.maxRange = range
		self.numberOfPassanagers = numberOfPassanagers
		self.realRange = int(self.maxRange - (self.maxRange * (AVERAGE_PASSANGER_RANGE_COST * self.numberOfPassanagers)))

	def setId(self, newId):
		self.id = newId
	
	def setVehicleValue(self, newValue):
		self.vehicleValue = newValue

	def setBatteryCapacity(self, newCapacity):
		self.batteryCapacity = newCapacity

	def setVehicleRange(self, newRange):
		self.maxRange = newRange
	
	def setNumberOfPassanagers(self, newPassanagers):
		self.numberOfPassanagers = newPassanagers
		self.realRange = int(self.maxRange - (self.maxRange * (AVERAGE_PASSANGER_RANGE_COST * self.numberOfPassanagers)))

	def toString(self):
		return  "Vehicle: " + self.id + "\tVehicle Value: €" + str(self.vehicleValue) + "\tTotal Battery Capacity: " + str(self.batteryCapacity) + "kWh" + "\tMax vehicle range: " + str(self.maxRange) + "KM" + "\tReal vehicle range: " + str(self.realRange) + "KM" + "\tNumber of Passanagers: " + str(self.numberOfPassanagers)

def generateVehicle(numberOfVehicles):
	vehicleData = []
	vehicleValueTolerance = 10000
	batteryCapacityTolerance = 15
	vehicleRangeTolerance = 50

	for i in range(numberOfVehicles):
		# Generate Values
		id = "C" + str(i)
		vehicleValue = random.randint(AVERAGE_VEHICLE_VALUE - vehicleValueTolerance, AVERAGE_VEHICLE_VALUE + vehicleValueTolerance)
		batteryCap = random.randint(AVERAGE_BATTERY_CAPACITY - batteryCapacityTolerance, AVERAGE_BATTERY_CAPACITY + batteryCapacityTolerance)
		vehicleRange = random.randint(AVERAGE_RANGE - vehicleRangeTolerance, AVERAGE_RANGE + vehicleRangeTolerance)
		passanagers = random.randint(0, 5)

		# Generate Vehicle
		vehicle = Private(id, vehicleValue, batteryCap, vehicleRange, passanagers)
		vehicleData.append(vehicle)
	return vehicleData

# start = time.time()
vehicleArray = generateVehicle(15)
for vehicle in vehicleArray:
	print(vehicle.toString())
# end = time.time()
# print("Elapsed:\t" + str(end - start) + "s")
