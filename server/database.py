from datetime import datetime
import os

import sqlite3
from sqlite3.dbapi2 import Timestamp
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
        self.cur.execute("CREATE TABLE IF NOT EXISTS session_info(id INT PRIMARY KEY, num_businesses INT, num_houses INT , num_infrastructure INT , num_vehicles INT,num_solar INT, num_wind INT ,session_current_time DATETIME)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY,session_id INT, time DATETIME, user_type VARCHAR(14), power_used INT,FOREIGN KEY(session_id) REFERENCES session_info(id) )")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS generators(id INT PRIMARY KEY,session_id INT,time DATETIME, generator_type VARCHAR(14), power_generated INT, FOREIGN KEY (session_id) REFERENCES session_info(id))")
        self.con.commit()

    def insert_session(self, session_id, num_businesses, num_houses, num_infrastructure, num_vehicles, num_solar, num_wind, session_current_time):
        """Insert session data into the session table

        Arguments: 

        time -- when the data was recorded (simulation time)

        session_dictionary -- python dictionary in format dict[type] = num_type
        """
        self.cur.execute("INSERT INTO session_info (id, num_businesses, num_houses, num_infrastructure, num_vehicles, num_solar, num_wind, session_current_time) VALUES(" +
                         f" '{session_id}' ,'{num_businesses}' , '{num_houses}' ,  '{num_infrastructure}' ,  '{num_vehicles}' ,  '{num_solar}' , '{num_wind}' , '{session_current_time}')")

        self.con.commit()

    def insert_usage(self, timestamp: datetime, usage_dictionary: dict, session_id:int):
        """Insert user data into the user table

        Arguments: 

        session_id -- foreign key referencing session_info(id)

        timestamp -- when the data was recorded (simulation time)

        usage_dictionary -- python dictionary in format dict[type] = power_used
        """
        sql = "INSERT INTO users (session_id, time, user_type, power_used) VALUES"
        comma = ""
        for key, value in usage_dictionary.items():
            sql += f" {comma}('{session_id}','{timestamp}', '{key}', {int(value)})"
            comma = "," # So that we update it next time

        self.cur.execute(sql)
        self.con.commit()
        pass

    def insert_generation(self, timestamp: datetime, generation_dictionary: dict, session_id:int):
        """Insert generator data into the generator table

        Arguments: 

        session_id -- foreign key referencing session_info(id)

        timestamp -- when the data was recorded (simulation time)

        generation_dictionary -- python dictionary in format dict[type] = power_generated
        """
        sql = "INSERT INTO generators (session_id, time, generator_type, power_generated) VALUES"
        comma = ""
        for key, value in generation_dictionary.items():
            # Temporary solution as int should be implied by update function
            sql += f" {comma}('{session_id}','{timestamp}','{key}',{int(value)})"
            comma = "," # So that we update it next time

        self.cur.execute(sql)
        self.con.commit()
        pass

    def select_info(self, type: str, id: int):
        """Get the number of 'type'

        Return: number of 'type'
        """

        if type == 'num_businesses':
            self.cur.execute("SELECT num_businesses  FROM session_info WHERE id = (" +f" '{id}' )")
        elif type == 'num_houses':
            self.cur.execute("SELECT num_houses  FROM session_info WHERE id = (" +f" '{id}' )")
        elif type == 'num_infrastructure':
            self.cur.execute("SELECT num_infrastructure  FROM session_info WHERE id = (" +f" '{id}' )")
        elif type == 'num_vehicles':
            self.cur.execute("SELECT num_vehicles  FROM session_info WHERE id = (" +f" '{id}' )")
        elif type == 'num_solar':
            self.cur.execute("SELECT num_solar  FROM session_info WHERE id = (" +f" '{id}' )")
        elif type == 'num_wind':
            self.cur.execute("SELECT num_wind  FROM session_info WHERE id = (" +f" '{id}' )")
        elif type == 'session_current_time':
            self.cur.execute("SELECT session_current_time  FROM session_info WHERE id = (" +f" '{id}' )")
        elif type == 'session_id':
            self.cur.execute("SELECT id  FROM session_info")

        return self.cur.fetchall()

    def update_time(self, time: datetime, id: int) :
        """Update time in session_info"""
        self.cur.execute("UPDATE session_info SET session_current_time = (" +f" '{time}' ) WHERE id = (" +f" '{id}');")
        self.con.commit()

    def __del__(self):
        """Delete database object & close the database"""
        self.con.close()
        pass
