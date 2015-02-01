#create sqlite3 database and table
#import sqlite3 library

import sqlite3

#create a new database
conn = sqlite3.connect("cars.db")

#get a cursor object to execute commands
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE inventory (make TEXT, model TEXT, quantity INT)""")

#close the database connection
conn.close()

