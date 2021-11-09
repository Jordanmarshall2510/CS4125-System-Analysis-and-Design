import sqlite3

class Database:
	def __init__(self):
		self.con = sqlite3.connect("../Server/database.db",check_same_thread=False)
		self.cur = self.con.cursor()

	def selectPowerHistory(self, type):
		self.cur.execute("SELECT power_used FROM users WHERE type = ? ORDER BY time", [type])
		return self.cur.fetchall()
		

	def __del__(self):
		self.con.close()