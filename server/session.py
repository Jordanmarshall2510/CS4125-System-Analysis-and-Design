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

		# Connect to database

		db = Database(sqlite=True)

		session_dictionary = {} 

		session_dictionary["num_businesses"] = 100
		session_dictionary["num_houses"] = 500
		session_dictionary["num_infrastructure"] = 50
		session_dictionary["num_vehicles"] = 200
		session_dictionary["num_solar"] = 1000
		session_dictionary["num_wind"] = 10
		session_dictionary["num_current_time"] = datetime.strptime("2022-10-18 05:24:30", "%Y-%m-%d %H:%M:%S")
		timestamp = datetime.strptime("2022-10-18 05:24:30", "%Y-%m-%d %H:%M:%S")

		db.insert_session(timestamp,session_dictionary)

		# Read city parameters
		with open(path, 'r') as json_file:
			conf = json.load(json_file)


		builder.construct_businesses((db.select_info("num_businesses"))[0][0])
		builder.construct_houses((db.select_info("num_houses"))[0][0])
		builder.construct_infrastructure((db.select_info("num_infrastructure"))[0][0])
		builder.construct_vehicles((db.select_info("num_vehicles"))[0][0])
		builder.construct_solar_panels((db.select_info("num_solar"))[0][0])
		builder.construct_wind_turbines((db.select_info("num_wind"))[0][0])

		# Build city
		city = builder.build()

		# Remove builder
		del builder		

		# Initialise timer
		timestamp = datetime.strptime(((db.select_info("num_current_time"))[0][0]), "%Y-%m-%d %H:%M:%S")
		for i in range(730):
			#Update the weather
			Weather.update_weather(conf['world']['weather']['weather'])
			
			#Update the season
			Seasons.update_season(timestamp)
			
			# Update City
			generation, usage = city.update(timestamp)

			# Put data into database
			db.insert_generation(timestamp, generation)
			db.insert_usage(timestamp, usage)

			# Progress time
			timestamp += timedelta(hours=1)
			
			# Update  database
			session_dictionary1 = {} 

			session_dictionary1["num_current_time"] = timestamp.strftime( "%Y-%m-%d %H:%M:%S")
			date = datetime.strptime("2022-10-18 05:24:30", "%Y-%m-%d %H:%M:%S")

			db.insert_session(date,session_dictionary1)

			# Update config file with weather
			conf['world']['weather']['weather'] = Weather.get_weather()
			with open(path, 'w') as json_file:
				json.dump(conf, json_file)

		del db