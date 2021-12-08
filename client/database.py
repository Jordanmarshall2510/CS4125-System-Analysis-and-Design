# Coded by Marcin Sek 18254187
import os
import sqlite3
import mysql.connector
from mysql.connector import errorcode

class Database:
	"""Database class dealing with select queries for the frontend"""
	def __init__(self, sqlite: bool):
		"""Initialze Database object & connect to database
		
		Arguments: sqlite -- Specifies if database is using mysql remotely or sqlite locally
		"""
		self.sqlite = sqlite
		if sqlite:
			path = os.path.dirname(os.path.realpath(__file__)) + "/../server/database.db"
			self.con = sqlite3.connect(path,check_same_thread=False)
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
		pass

	def select_used_power_history(self, type: str):
		"""Get the Used_Power of a user

		Arguments: type -- the type of user being search for

		Return: list of power_used sorted by time
		"""
		self.cur.execute(f"SELECT power_used FROM users WHERE user_type = '{type}' ORDER BY time")
		return self.cur.fetchall()

	def select_generated_power_history(self, type: str):
		"""Get the Generated_Power of a user

		Arguments: type -- the type of user being search for

		Return: list of power_generated sorted by time
		"""
		self.cur.execute(f"SELECT power_generated FROM generators WHERE generator_type = '{type}' ORDER BY time")
		return self.cur.fetchall()
		
	def select_total_used_power_history(self):
		"""Get the total power_used per timestamp

		Return: list of total power_used sorted by time
		"""
		self.cur.execute("SELECT SUM(power_used) AS total FROM users GROUP BY time")
		return self.cur.fetchall()

	def select_total_generated_power_history(self):
		"""Get the total power_generated per timestamp

		Return: list of total power_generated sorted by time
		"""
		self.cur.execute("SELECT SUM(power_generated) AS total FROM generators GROUP BY time")
		return self.cur.fetchall()

	def select_info(self, type: str, id: int):
		"""Get the number of 'type'

		Return: number of 'type'
		"""

		if type == 'num_businesses':
			self.cur.execute("SELECT num_businesses  FROM session_info WHERE id = ?;", (id,))
		elif type == 'num_houses':
			self.cur.execute("SELECT num_houses  FROM session_info WHERE id =  ?;", (id,))
		elif type == 'num_infrastructure':
			self.cur.execute("SELECT num_infrastructure  FROM session_info WHERE id = ?;", (id,))
		elif type == 'num_vehicles':
			self.cur.execute("SELECT num_vehicles  FROM session_info WHERE id = ?;", (id,))
		elif type == 'num_solar':
			self.cur.execute("SELECT num_solar  FROM session_info WHERE id = ?;", (id,))
		elif type == 'num_wind':
			self.cur.execute("SELECT num_wind  FROM session_info WHERE id = ?;", (id,))
		elif type == 'session_current_time':
			self.cur.execute("SELECT session_current_time  FROM session_info WHERE id = ?;", (id,))
		elif type == 'session_id':
			self.cur.execute("SELECT id  FROM session_info")

		return self.cur.fetchall()


	def __del__(self):
		"""Delete database object & close the database"""
		self.con.close()
		pass