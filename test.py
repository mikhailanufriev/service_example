import pyodbc
import time
import random
from pathlib import Path
from monitorWinservice import monitorWinservice
from datetime import datetime

class Sql:
    def __init__(self, database, server=""):
        self.cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                   "Trusted_Connection=yes;")
        self.query = "-- {}\n\n-- Made in Python".format(datetime.now().strftime("%d/%m/%Y"))

server = 'DESKTOP-HT8OSHB\HOMESERVER'
database = 'testdb'
username = 'user1'
password = 'qwer'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


cursor = cnxn.cursor()
query = ("SELECT [id],[startdate],[enddate],[message],[errorflag],[name] FROM [dbo].[logs]")
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    logs_id = row[0]
    logs_startdate = row[1]
    logs_enddate = row [2]
    logs_message = row [3]
    logs_errorflag = row[4]
    logs_name = row[5]

    logfile = open("logssql.txt", "a")
    logfile.write(str(row[0]) + " " + str(row[1]) + " " + str(row[2])+ " " + str(row[3])+ " " + str(row[4])+ " " + str(row[5]) + "\n")

cnxn.close()
