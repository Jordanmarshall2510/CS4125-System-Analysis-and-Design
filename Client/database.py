# Coded by Marcin Sek 18254187
import os
import sqlite3

class Database:
	"""Database class dealing with select queries for the frontend"""
	def __init__(self):
		"""Initialze Database object & connect to database"""
		path = os.path.dirname(os.path.realpath(__file__)) + "/../Server/database.db"
		self.con = sqlite3.connect(path,check_same_thread=False)
		self.cur = self.con.cursor()

	def selectUsedPowerHistory(self, type : str):
		"""Get the Used_Power of a user

		Arguments: type -- the type of user being search for

		Return: list of power_used sorted by time
		"""
		self.cur.execute("SELECT power_used FROM users WHERE type = ? ORDER BY time", [type])
		return self.cur.fetchall()

	def selectGeneratedPowerHistory(self, type : str):
		"""Get the Generated_Power of a user

		Arguments: type -- the type of user being search for

		Return: list of power_generated sorted by time
		"""
		self.cur.execute("SELECT power_generated FROM generators WHERE type = ? ORDER BY time", [type])
		return self.cur.fetchall()
		
	def selectTotalUsedPowerHistory(self):
		"""Get the total power_used per timestamp

		Return: list of total power_used sorted by time
		"""
		self.cur.execute("SELECT SUM(power_used) AS total FROM users GROUP BY time")
		return self.cur.fetchall()

	def selectTotalGeneratedPowerHistory(self):
		"""Get the total power_generated per timestamp

		Return: list of total power_generated sorted by time
		"""
		self.cur.execute("SELECT SUM(power_generated) AS total FROM generators GROUP BY time")
		return self.cur.fetchall()

	def __del__(self):
		"""Delete database object & close the database"""
		self.con.close()