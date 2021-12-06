from datetime import datetime
import os

import sqlite3
import mysql.connector
from mysql.connector import errorcode

class Database:
	"""Database class dealing with insert queries for the simulation"""
	def __init__(self, sqlite: bool):
		"""Initialze Database object & connect to database
		
		Arguments: sqlite -- Specifies if database is using mysql remotely or sqlite locally
		"""
		self.sqlite = sqlite
		if sqlite:
			path = os.path.dirname(os.path.realpath(__file__)) + "/database.db"
			self.con = sqlite3.connect(path)
		else:
			try:
				self.con = mysql.connector.connect(
					host="localhost",
					user="SimUser",
					password="!Sim_Password21",
					database="smart_city"
				)
			except mysql.connector.Error as err:
				if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
					print("Something is wrong with your user name or password")
				elif err.errno == errorcode.ER_BAD_DB_ERROR:
					print("Database does not exist")
				else:
					print(err)

		self.cur = self.con.cursor()
		if sqlite:
			self.setup_database()
		pass

	def setup_database(self):
		"""Setup the database if it doesnt exist already"""
		self.cur.execute("CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY, time DATETIME, user_type VARCHAR(14), power_used INT)")
		self.cur.execute("CREATE TABLE IF NOT EXISTS generators(id INT PRIMARY KEY, time DATETIME, generator_type VARCHAR(14), power_generated INT)")
		self.con.commit()
		pass

	def insert_usage(self, timestamp: datetime, usage_dictionary : dict):
		"""Insert user data into the user table

		Arguments: 
			
		timestamp -- when the data was recorded (simulation time)
		
		usage_dictionary -- python dictionary in format dict[type] = power_used
		"""
		sql = "INSERT INTO users (time, user_type, power_used) VALUES"
		comma = ""
		for key, value in usage_dictionary.items():
			sql += f" {comma}('{timestamp}', '{key}', {int(value)})"
			comma = "," # So that we update it next time

		self.cur.execute(sql)
		self.con.commit()
		pass

	def insert_generation(self, timestamp: datetime, generation_dictionary: dict):
		"""Insert generator data into the generator table

		Arguments: 
			
		timestamp -- when the data was recorded (simulation time)
		
		generation_dictionary -- python dictionary in format dict[type] = power_generated
		"""
		sql = "INSERT INTO generators (time, generator_type, power_generated) VALUES"
		comma = ""
		for key, value in generation_dictionary.items():
			sql += f" {comma}('{timestamp}','{key}',{int(value)})" # Temporary solution as int should be implied by update function
			comma = "," # So that we update it next time

		self.cur.execute(sql)
		self.con.commit()
		pass

	def __del__(self):
		"""Delete database object & close the database"""
		self.con.close()
		pass