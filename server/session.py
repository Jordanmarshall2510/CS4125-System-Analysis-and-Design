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

	# Open config file 

	with open(path, 'r') as json_file:
		conf = json.load(json_file)

	session_id = conf['session_info']['id']
	db = None
	city = None
	weather = None
	
	@staticmethod
	def init_database(host=None, user=None, password=None, database=None, remote=True):

		# Add city parameters to database

		num_businesses = 100
		num_houses = 500
		num_infrastructure = 50
		num_vehicles = 200
		num_solar = 1000
		num_wind = 10
		session_current_time = datetime.strptime("2022-10-18 05:24:30", "%Y-%m-%d %H:%M:%S")

		Session.db = Database(host, user, password, database, sqlite=remote)

		if len(Session.db.select_info("session_id", Session.session_id)) == 0:
			Session.db.insert_session(Session.session_id, num_businesses, num_houses, num_infrastructure, num_vehicles,num_solar, num_wind,session_current_time)

	@staticmethod
	def init_simulation():
		# Prepare city builder
		builder = CityBuilder()

		# Initialze weather
		weather = Weather()
		season = Seasons()
		season.init()
		weather.init()
		
		# Get info from database to build city

		builder.construct_businesses((Session.db.select_info("num_businesses", Session.session_id))[0][0])
		builder.construct_houses((Session.db.select_info("num_houses", Session.session_id))[0][0])
		builder.construct_infrastructure((Session.db.select_info("num_infrastructure", Session.session_id))[0][0])
		builder.construct_vehicles((Session.db.select_info("num_vehicles", Session.session_id))[0][0])
		builder.construct_solar_panels((Session.db.select_info("num_solar", Session.session_id))[0][0])
		builder.construct_wind_turbines((Session.db.select_info("num_wind", Session.session_id))[0][0])

		# Build city
		Session.city = builder.build()	

	@staticmethod
	def run():
		# Initialise timer
		timestamp = datetime.strptime(str(Session.db.select_info("session_current_time", Session.session_id)[0][0]), "%Y-%m-%d %H:%M:%S")
		for i in range(730):
			#Update the weather
			Weather.update_weather(Session.conf['world']['weather']['weather'])
			
			#Update the season
			Seasons.update_season(timestamp)
			
			# Update City
			generation, usage = Session.city.update(timestamp)

			# Put data into database
			Session.db.insert_generation(timestamp, generation, Session.session_id)
			Session.db.insert_usage(timestamp, usage, Session.session_id)

			# Progress time
			timestamp += timedelta(hours=1)
			# Update  database
			Session.db.update_time(timestamp, Session.session_id)

			# Update config file with weather
			Session.conf['world']['weather']['weather'] = Weather.get_weather()
			with open(path, 'w') as json_file:
				json.dump(Session.conf, json_file)