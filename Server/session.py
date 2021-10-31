import threading
from datetime import timedelta, datetime
from ElectricityGenerator.distribution import *
from ElectricityUser.businesses import generateBusinessData
from ElectricityUser.houses import generateHouseData
from ElectricityUser.infrastrucure import generateInfrastructureData
from ElectricityUser.vehicles import generateVehicleData

# TODO:
#   Create class for session so we can run multiple instances

path = os.path.dirname(os.path.realpath(__file__)) + "//config.json"

# Craete user array
arrUsers = []

# Load users
with open(path) as json_file:
    conf = json.load(json_file)

    arrUsers.append(generateBusinessData(conf['session']['electricityUser']['businesses']))
    arrUsers.append(generateHouseData(conf['session']['electricityUser']['houses']))
    arrUsers.append(generateInfrastructureData(conf['session']['electricityUser']['infrastructure']))
    arrUsers.append(generateVehicleData(conf["session"]['electricityUser']['vehicles']))

# Initialise timer
timestamp = datetime.today()

while (True):
    # Progress time
    timestamp += datetime.timedelta(hours=1)

    # Update Distribution
    distribution.update(timestamp) # Might need a change

    # Update Users
    for user in arrUsers:
        user.update(timestamp)

    # Put data into database
