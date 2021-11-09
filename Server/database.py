import sqlite3

class Database:
	def __init__(self):
		self.con = sqlite3.connect("database.db")
		self.cur = self.con.cursor()
		self.setupDatabase()

	def setupDatabase(self):
		self.cur.execute("CREATE TABLE IF NOT EXISTS users(time DATETIME, type VARCHAR(16), power_used INT)")
		self.cur.execute("CREATE TABLE IF NOT EXISTS generators(time DATETIME, type VARCHAR(16), power_generated INT)")
		self.con.commit()
		pass

	def insertUsage(self, timestamp, usageDictionary):
		for key in usageDictionary:
			self.cur.execute("INSERT INTO users VALUES(?, ?, ?)", (timestamp, key, usageDictionary[key]))

		self.con.commit()

	def insertGeneration(self, timestamp, generationDictionary):
		for key in generationDictionary:
			self.cur.execute("INSERT INTO users VALUES(?, ?, ?)", (timestamp, key, generationDictionary[key]))

		self.con.commit()

	def __del__(self):
		self.con.close()