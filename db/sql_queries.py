import sqlite3

con = sqlite3.connect('hotel.db')

cur = con.cursor()

cur.execute("SELECT * FROM room WHERE id NOT IN (SELECT room_id FROM reservation)")
for line in cur.fetchall():
    print(f"{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}")

print("\n\n\n")

cur.execute("""SELECT firstname, lastname, passport FROM client WHERE id IN (SELECT client_id FROM reservation WHERE id IN (SELECT reservation_id FROM bill))""")
for line in cur.fetchall():
    print(f"{line[0]}\t{line[1]}\t{line[2]}")

print("\n\n\n")

cur.execute("""SELECT * FROM room WHERE cost_per_day < 3000 AND (type = "double" OR type = "twin")""")
for line in cur.fetchall():
    print(f"{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}\t")