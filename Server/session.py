# from datetime import timedelta, datetime
from ElectricityGenerator.distribution import *
from ElectricityUser.businesses import generateBusinessData
from ElectricityUser.houses import generateHouses
from ElectricityUser.infrastrucure import generateInfrastructureData
from ElectricityUser.vehicles import Vehicle

path = os.path.dirname(os.path.realpath(__file__)) + "//config.json"

# Craete user array
arrUsers = []

# Load users
with open(path) as json_file:
    conf = json.load(json_file)

    arrUsers += generateBusinessData(conf['session']['electricityUser']['businesses'])
    arrUsers += generateHouses(conf['session']['electricityUser']['houses'])
    arrUsers += arrUsers, generateInfrastructureData(conf['session']['electricityUser']['infrastucture'])
    arrUsers += arrUsers, Vehicle.generateUsers(conf["session"]['electricityUser']['vehicles'])

# Initialise timer
# timestamp = datetime.today()

while (True):
    # Progress time
    # timestamp += datetime.timedelta(hours=1)

    # Update Distribution
    # distribution.update(timestamp) # Might need a change

    # Update Users
    for user in arrUsers:
        electricityUsed = user.update(100)
        print(electricityUsed)
        

    # Put data into database
