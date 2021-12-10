import os
import json
from threading import Thread
from datetime import datetime, timedelta
from server.city import CityBuilder
from server.world.weather import Weather
from server.world.seasons import Seasons
from server.database import Database

path = os.path.dirname(os.path.realpath(__file__)) + "//config.json"

class Session():

	
	@staticmethod
	def init():

		# Prepare city builder
		builder = CityBuilder()

		# Initialze weather
		weather = Weather()
		season = Seasons()
		season.init()
		weather.init()


		# Open config file 

		with open(path, 'r') as json_file:
			conf = json.load(json_file)

		# Add city parameters to database

		num_businesses = 100
		num_houses = 500
		num_infrastructure = 50
		num_vehicles = 200
		num_solar = 1000
		num_wind = 10
		session_id = (conf['session_info']['id'])
		session_current_time = datetime.strptime("2022-10-18 05:24:30", "%Y-%m-%d %H:%M:%S")
		timestamp = datetime.strptime("2022-10-18 05:24:30", "%Y-%m-%d %H:%M:%S")

		# Connect to database

		db = Database(sqlite=True)

		if len(db.select_info("session_id", session_id)) == 0:
			db.insert_session(session_id, num_businesses, num_houses, num_infrastructure, num_vehicles,num_solar, num_wind,session_current_time)

		# Get info from database to build city

		builder.construct_businesses((db.select_info("num_businesses", session_id))[0][0])
		builder.construct_houses((db.select_info("num_houses", session_id))[0][0])
		builder.construct_infrastructure((db.select_info("num_infrastructure", session_id))[0][0])
		builder.construct_vehicles((db.select_info("num_vehicles", session_id))[0][0])
		builder.construct_solar_panels((db.select_info("num_solar", session_id))[0][0])
		builder.construct_wind_turbines((db.select_info("num_wind", session_id))[0][0])

		# Build city
		city = builder.build()

		# Remove builder
		del builder		

		# Initialise timer
		timestamp = datetime.strptime(str(db.select_info("session_current_time", session_id)[0][0]), "%Y-%m-%d %H:%M:%S")
		for i in range(730):
			#Update the weather
			Weather.update_weather(conf['world']['weather']['weather'])
			
			#Update the season
			Seasons.update_season(timestamp)
			
			# Update City
			generation, usage = city.update(timestamp)

			# Put data into database
			db.insert_generation(timestamp, generation, session_id)
			db.insert_usage(timestamp, usage, session_id)

			# Progress time
			timestamp += timedelta(hours=1)
			# Update  database
			db.update_time(timestamp, session_id)

			# Update config file with weather
			conf['world']['weather']['weather'] = Weather.get_weather()
			with open(path, 'w') as json_file:
				json.dump(conf, json_file)

		del db