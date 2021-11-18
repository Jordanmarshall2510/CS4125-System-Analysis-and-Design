## Coded by Marcin Sek 18254187
# TODO:
#	Reduce range based on temperature
#	NOTE: Winter / cold weather can cause a decrease of up to 25%
#	Reduce battery performance overtime
#	NOTE: Battery degredation on average is 1% SOH per 6 months
#	
#	***Extend electricityUsers and import required functions (update & getElectricityUsed)***

# import time
import random
import json
import os

from ElectricityUser.electricityuser import ElectricityUser

class Vehicle(ElectricityUser):
	# Read initialising data from json
	path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityUser")[0] + "config.json"
	with open(path) as json_file:
		conf = json.load(json_file)
		
	# Average electric car value. Units in EURO
	AVERAGE_VEHICLE_VALUE = conf["electricityUser"]["vehicles"]["averageVehicleValue"]

	# Average electric car battery capacity. Units in kWh
	AVERAGE_BATTERY_CAPACITY = conf["electricityUser"]["vehicles"]["averageBatteryCapacity"]

	# Average electric car range. Units in KM
	AVERAGE_RANGE = conf["electricityUser"]["vehicles"]["averageRange"]

	# Average decrease in range per person. Units %
	AVERAGE_PASSANGER_RANGE_COST = conf["electricityUser"]["vehicles"]["averagePassengerRangeCost"]

	def __init__(self, id, vehicleValue, batteryCapacity, range, numberOfPassanagers):
		"""Intialize a vechicle object"""
		self.id = id
		self.vehicleValue = vehicleValue
		self.batteryCapacity = batteryCapacity
		self.maxRange = range
		self.numberOfPassanagers = numberOfPassanagers
		self.realRange = int(self.maxRange - (self.maxRange * self.AVERAGE_PASSANGER_RANGE_COST * self.numberOfPassanagers))

	# TODO: implement update and getElectricityUsed methods
	def update(self, date):
		return -1

	def getElectricityUsed(self):
		return -1

	def setId(self, newId):
		"""Change vechicle ID"""
		self.id = newId
	
	def setVehicleValue(self, newValue):
		"""Change vechicle value"""
		self.vehicleValue = newValue

	def setBatteryCapacity(self, newCapacity):
		"""Change vechicle battery capacity"""
		self.batteryCapacity = newCapacity

	def setVehicleRange(self, newRange):
		"""Change vechicle range"""
		self.maxRange = newRange
	
	def setNumberOfPassanagers(self, newPassanagers):
		"""Change number of occupants"""
		self.numberOfPassanagers = newPassanagers
		self.realRange = int(self.maxRange - (self.maxRange * (self.AVERAGE_PASSANGER_RANGE_COST * self.numberOfPassanagers)))

	def generateUsers(numberOfVehicles):
		vehicleData = []
		vehicleValueTolerance = 10000
		batteryCapacityTolerance = 15
		vehicleRangeTolerance = 50

		for i in range(numberOfVehicles):
			# Generate Values
			id = "C" + str(i)
			vehicleValue = random.randint(Vehicle.AVERAGE_VEHICLE_VALUE - vehicleValueTolerance, Vehicle.AVERAGE_VEHICLE_VALUE + vehicleValueTolerance)
			batteryCap = random.randint(Vehicle.AVERAGE_BATTERY_CAPACITY - batteryCapacityTolerance, Vehicle.AVERAGE_BATTERY_CAPACITY + batteryCapacityTolerance)
			vehicleRange = random.randint(Vehicle.AVERAGE_RANGE - vehicleRangeTolerance, Vehicle.AVERAGE_RANGE + vehicleRangeTolerance)
			passanagers = random.randint(0, 5)

			# Generate Vehicle
			vehicle = Vehicle(id, vehicleValue, batteryCap, vehicleRange, passanagers)
			vehicleData.append(vehicle)
		return vehicleData

	def toString(self):
		"""Return vechicle as a string"""
		return  "Vehicle: " + self.id + "\tVehicle Value: €" + str(self.vehicleValue) + "\tTotal Battery Capacity: " + str(self.batteryCapacity) + "kWh" + "\tMax vehicle range: " + str(self.maxRange) + "KM" + "\tReal vehicle range: " + str(self.realRange) + "KM" + "\tNumber of Passanagers: " + str(self.numberOfPassanagers)
