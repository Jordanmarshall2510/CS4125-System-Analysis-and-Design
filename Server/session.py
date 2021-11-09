import os
import json
from datetime import datetime, timedelta
from ElectricityUser.businesses import Business
from ElectricityUser.houses import House
from ElectricityUser.infrastrucure import Infrastructure
from ElectricityUser.vehicles import Vehicle
from ElectricityGenerator.distribution import Distribution
from databasemanager import insertUsage, insertGeneration

path = os.path.dirname(os.path.realpath(__file__)) + "//config.json"

# Create user array
arrUsers = []

# Set distribution
distribution = Distribution()

# Load users
with open(path) as json_file:
    conf = json.load(json_file)

    arrUsers += Business.generateUsers(conf['session']['electricityUser']['businesses'])
    arrUsers += House.generateUsers(conf['session']['electricityUser']['houses'])
    arrUsers += Infrastructure.generateUsers(conf['session']['electricityUser']['infrastucture'])
    arrUsers += Vehicle.generateUsers(conf["session"]['electricityUser']['vehicles'])

# Initialise timer
timestamp = datetime.now()
while (True):
    # Create dictionary for the day
    dict = {}

    # Update Distribution
    distribution.update(timestamp) # Might need a change

    # Update Users
    for user in arrUsers:
        electricityUsed = user.update(timestamp)
        if type(user).__name__ in dict:
            dict[type(user).__name__] += electricityUsed
        else:
            dict[type(user).__name__] = electricityUsed

    print("=================================")
    print(f"Timestamp: {timestamp}")
    print("-- Users --")
    for key in dict:
        print(f"Total usage from {key}: {dict[key]}")
    print("-- Generators --")
    # TODO: print the generator data
    print("=================================")

    # Put data into database
    insertUsage(timestamp, dict)
    # insertGeneration(timestamp, dict) # Will this be a new dictionary ? (How to access solar and wind)

    # Progress time
    timestamp += timedelta(hours=1)