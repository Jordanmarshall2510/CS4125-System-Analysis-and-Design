import os
import json
from datetime import datetime, timedelta
from city import CityBuilder
from World.weather import Weather
from database import Database

path = os.path.dirname(os.path.realpath(__file__)) + "//config.json"

# Prepare city builder
builder = CityBuilder()

# Initialze weather
weather = Weather()

# Read city parameters
with open(path, 'r') as json_file:
    conf = json.load(json_file)

    builder.construct_businesses(
        conf['session']['electricity_user']['businesses'])
    builder.construct_houses(conf['session']['electricity_user']['houses'])
    builder.construct_infrastructure(
        conf['session']['electricity_user']['infrastructure'])
    builder.construct_vehicles(conf["session"]['electricity_user']['vehicles'])
    builder.construct_solar_panels(
        conf["session"]['electricity_generator']['solar'])
    builder.construct_wind_turbines(
        conf["session"]["electricity_generator"]["wind"])

# Build city
city = builder.build()

# Remove builder
del builder

# Connect to database
db = Database()

session_dictionary = {} 
session_dictionary["num_businesess"] = 100
session_dictionary["num_houses"] = 500
session_dictionary["num_infrastructure"] = 50
session_dictionary["num_vehicles"] = 200
session_dictionary["num_solar"] = 1000
session_dictionary["num_wind"] = 10
timestamp = datetime.strptime("2022-10-18 05:24:30", "%Y-%m-%d %H:%M:%S")

insert_session(timestamp,session_dictionary)


# Initialise timer
timestamp = datetime.strptime(conf['session']['time'], "%Y-%m-%d %H:%M:%S")
for i in range(730):
    # Update the weather and season
    Weather.update_weather(conf['world']['weather']['weather'], timestamp)

    # Update City
    generation, usage = city.update(timestamp)

    # Put data into database
    db.insert_generation(timestamp, generation)
    db.insert_usage(timestamp, usage)

    # Progress time
    timestamp += timedelta(hours=1)

    # Update Json files
    conf['session']['time'] = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    conf['world']['weather']['weather'] = Weather.get_weather()
    with open(path, 'w') as json_file:
        json.dump(conf, json_file)

del db
