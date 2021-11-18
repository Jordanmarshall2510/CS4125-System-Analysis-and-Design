import sqlite3
import os

class Database:
	def __init__(self):
		"""Initialze Database object & connect to database"""
		path = os.path.dirname(os.path.realpath(__file__)) + "/database.db"
		self.con = sqlite3.connect(path)
		self.cur = self.con.cursor()
		self.setupDatabase()

	def setupDatabase(self):
		"""Setup the database if it doesnt exist already"""
		self.cur.execute("CREATE TABLE IF NOT EXISTS users(time DATETIME, type VARCHAR(14), power_used INT)")
		self.cur.execute("CREATE TABLE IF NOT EXISTS generators(time DATETIME, type VARCHAR(14), power_generated INT)")
		self.con.commit()
		pass

	def insertUsage(self, timestamp, usageDictionary):
		"""Insert user data into the user table

		Arguments: 
			
		timestamp -- when the data was recorded (simulation time)
		
		usageDictionary -- python dictionary in format dict[type] = power_used
		"""
		for key in usageDictionary:
			self.cur.execute("INSERT INTO users VALUES(?, ?, ?)", (timestamp, key, usageDictionary[key]))

		self.con.commit()

	def insertGeneration(self, timestamp, generationDictionary):
		"""Insert generator data into the generator table

		Arguments: 
			
		timestamp -- when the data was recorded (simulation time)
		
		generationDictionary -- python dictionary in format dict[type] = power_generated
		"""
		for key in generationDictionary:
			self.cur.execute("INSERT INTO generators VALUES(?, ?, ?)", (timestamp, key, generationDictionary[key]))

		self.con.commit()

	def __del__(self):
		"""Delete database object & close the database"""
		self.con.close()