# from datetime import timedelta, datetime
import os
import json
from ElectricityUser.businesses import Business
from ElectricityUser.houses import House
from ElectricityUser.infrastrucure import Infrastructure
from ElectricityUser.vehicles import Vehicle
from ElectricityGenerator.distribution import Distribution

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
# timestamp = datetime.today()

while (True):
    # Progress time
    # timestamp += datetime.timedelta(hours=1)

    # Update Distribution
    # distribution.update(timestamp) # Might need a change

    # Update Users
    for user in arrUsers:
        distribution.update(100)
        electricityUsed = user.update(100)        

    # Put data into database
