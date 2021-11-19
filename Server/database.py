from datetime import datetime
import sqlite3
import os

class Database:
	"""Database class dealing with insert queries for the simulation"""
	def __init__(self):
		"""Initialze Database object & connect to database"""
		path = os.path.dirname(os.path.realpath(__file__)) + "/database.db"
		self.con = sqlite3.connect(path)
		self.cur = self.con.cursor()
		self.setup_database()

	def setup_database(self):
		"""Setup the database if it doesnt exist already"""
		self.cur.execute("CREATE TABLE IF NOT EXISTS users(time DATETIME, type VARCHAR(14), power_used INT)")
		self.cur.execute("CREATE TABLE IF NOT EXISTS generators(time DATETIME, type VARCHAR(14), power_generated INT)")
		self.con.commit()
		pass

	def insert_usage(self, timestamp : datetime, usage_dictionary : dict):
		"""Insert user data into the user table

		Arguments: 
			
		timestamp -- when the data was recorded (simulation time)
		
		usage_dictionary -- python dictionary in format dict[type] = power_used
		"""
		for key in usage_dictionary:
			self.cur.execute("INSERT INTO users VALUES(?, ?, ?)", (timestamp, key, usage_dictionary[key]))

		self.con.commit()

	def insert_generation(self, timestamp : datetime, generation_dictionary : dict):
		"""Insert generator data into the generator table

		Arguments: 
			
		timestamp -- when the data was recorded (simulation time)
		
		generation_dictionary -- python dictionary in format dict[type] = power_generated
		"""
		for key in generation_dictionary:
			self.cur.execute("INSERT INTO generators VALUES(?, ?, ?)", (timestamp, key, generation_dictionary[key]))

		self.con.commit()

	def __del__(self):
		"""Delete database object & close the database"""
		self.con.close()