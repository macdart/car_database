import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    

    for row in c.execute("SELECT  model, quantity from inventory WHERE make='Ford'"):
        print row
