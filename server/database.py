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
		self.cur.execute("CREATE TABLE IF NOT EXISTS session_info(time DATETIME,type VARCHAR(14), number_of_type INT)")
		self.con.commit()

	def insert_session(self, time: datetime, session_dictionary : dict):
		"""Insert session data into the session table

		Arguments: 
			
		time -- when the data was recorded (simulation time)
		
		session_dictionary -- python dictionary in format dict[type] = num_type
		"""
		for key in session_dictionary:
			self.cur.execute("INSERT INTO session_info VALUES(?, ?, ?)", (time, key, session_dictionary[key]))
		self.con.commit()

	def insert_usage(self, timestamp: datetime, usage_dictionary : dict):
		"""Insert user data into the user table

		Arguments: 
			
		timestamp -- when the data was recorded (simulation time)
		
		usage_dictionary -- python dictionary in format dict[type] = power_used
		"""
		for key, value in usage_dictionary.items():
			self.cur.execute("INSERT INTO users VALUES(?, ?, ?)", (timestamp, key, value))

		self.con.commit()

	def insert_generation(self, timestamp: datetime, generation_dictionary: dict):
		"""Insert generator data into the generator table

		Arguments: 
			
		timestamp -- when the data was recorded (simulation time)
		
		generation_dictionary -- python dictionary in format dict[type] = power_generated
		"""
		for key, value in generation_dictionary.items():
			self.cur.execute("INSERT INTO generators VALUES(?, ?, ?)", (timestamp, key, value))

		self.con.commit()

	def select_info(self, type: str):
		"""Get the number of businesses

		Return: number of businesses
		"""
		self.cur.execute("SELECT number_of_type FROM session_info WHERE type = ?", [type])
		return self.cur.fetchall()


	def __del__(self):
		"""Delete database object & close the database"""
		self.con.close()