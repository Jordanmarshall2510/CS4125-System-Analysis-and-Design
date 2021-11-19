import os
import json
from datetime import datetime, timedelta
from ElectricityUser.businesses import Business
from ElectricityUser.houses import House
from ElectricityUser.infrastrucure import Infrastructure
from ElectricityUser.vehicles import Vehicle
from ElectricityGenerator.distribution import Distribution
from World.weather import Weather
from database import Database

path = os.path.dirname(os.path.realpath(__file__)) + "//config.json"

# Create user array
users_array = []

# Set distribution
distribution = Distribution()

# Initialze weather
weather = Weather()

# Load users
with open(path, 'r') as json_file:
	conf = json.load(json_file)

	users_array += Business.generate_users(conf['session']['electricity_user']['businesses'])
	users_array += House.generate_users(conf['session']['electricity_user']['houses'])
	users_array += Infrastructure.generate_users(conf['session']['electricity_user']['infrastructure'])
	users_array += Vehicle.generate_users(conf["session"]['electricity_user']['vehicles'])

# Connect to database
db = Database()

# Initialise timer
timestamp = datetime.strptime(conf['session']['time'], "%Y-%m-%d %H:%M:%S")
for i in range(730):
	# Create dictionary for the Users
	user_dictionary = {}

	# Retrieve dictionary for the Generators
	generator_dictionary = distribution.update(timestamp) # Might need a change

	# Update Users
	for user in users_array:
		electricityUsed = user.update(timestamp)
		if type(user).__name__ in user_dictionary:
			user_dictionary[type(user).__name__] += electricityUsed
		else:
			user_dictionary[type(user).__name__] = electricityUsed

	# Put data into database
	db.insert_usage(timestamp, user_dictionary)
	db.insert_generation(timestamp, generator_dictionary) # Will this be a new dictionary ? (How to access solar and wind)

	# Progress time
	timestamp += timedelta(hours=1)

	# Update Json files
	conf['session']['time'] = timestamp.strftime("%Y-%m-%d %H:%M:%S")
	with open(path, 'w') as json_file:
		json.dump(conf, json_file)

del db