import os
import json
from datetime import datetime, timedelta
from ElectricityUser.businesses import Business
from ElectricityUser.houses import House
from ElectricityUser.infrastrucure import Infrastructure
from ElectricityUser.vehicles import Vehicle
from ElectricityGenerator.distribution import Distribution
from database import Database

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

# Connect to database
db = Database()

# Initialise timer
timestamp = datetime.now()
for i in range(10):
    # Create dictionary for the Users
    userDict = {}

    # Retrieve dictionary for the Generators
    generatorDict = distribution.update(timestamp) # Might need a change

    # Update Users
    for user in arrUsers:
        electricityUsed = user.update(timestamp)
        if type(user).__name__ in userDict:
            userDict[type(user).__name__] += electricityUsed
        else:
            userDict[type(user).__name__] = electricityUsed

    # Put data into database
    db.insertUsage(timestamp, userDict)
    db.insertGeneration(timestamp, generatorDict) # Will this be a new dictionary ? (How to access solar and wind)

    # Progress time
    timestamp += timedelta(hours=1)

del db