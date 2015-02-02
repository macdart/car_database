import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("INSERT INTO inventory VALUES('Ford', 'Ranger', 7)")
    c.execute("INSERT INTO inventory VALUES('Ford', 'Focus', 18)")
    c.execute("INSERT INTO inventory VALUES('Ford', 'Fusion', 2340)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'Accord', 1)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'Salisbury', 17)")
