import sqlite3

class Database:
	def __init__(self):
		self.con = sqlite3.connect("../Server/database.db")
		self.cur = self.con.cursor()

	def selectUsedPowerHistory(self, type):
		self.cur.execute("SELECT time, power_used FROM users WHERE type = ? ORDER BY time", [type])
		return self.cur.fetchall()

	def selectGeneratedPowerHistory(self, type):
		self.cur.execute("SELECT time, power_used FROM generators WHERE type = ? ORDER BY time", [type])
		return self.cur.fetchall()
		
	def selectTotalUsedPowerHistory(self):
		self.cur.execute("SELECT time, SUM(power_used) AS total FROM users GROUP BY time")
		return self.cur.fetchall()

	def selectTotalGeneratedPowerHistory(self):
		self.cur.execute("SELECT time, SUM(power_used) AS total FROM generators GROUP BY time")
		return self.cur.fetchall()

	def __del__(self):
		self.con.close()