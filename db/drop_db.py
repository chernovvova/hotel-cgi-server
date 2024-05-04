import sqlite3

con = sqlite3.connect("hotel.db")

cur = con.cursor()

cur.execute("DROP TABLE client")
cur.execute("DROP TABLE room")
cur.execute("DROP TABLE reservation")
cur.execute("DROP TABLE bill")

con.commit()
con.close()