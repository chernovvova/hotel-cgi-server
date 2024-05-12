#!/usr/bin/env python

import sqlite3
import cgi

form = cgi.FieldStorage()
reservation_date = form.getfirst("reservation_date", "не задано")
checkin_date = form.getfirst("checkin_date", "не задано")
checkout_date = form.getfirst("checkout_date", "не задано")
room_id = form.getfirst("room_id", "не задано")
client_id = form.getfirst("client_id", "не задано")
con = sqlite3.connect('hotel.db')

cur = con.cursor()
sql = "INSERT INTO reservation(reservation_date, checkin_date, checkout_date, room_id, client_id) VALUES (?, ?, ?, ?, ?)"
cur.execute(sql, (reservation_date, checkin_date, checkout_date, room_id, client_id))
con.commit()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="UTF-8">
<title>Обработка книг </title>
</head>
<body>""")
print("<div>Бронь успешно добавлена в базу данных</div>")
print("""</body> </html>""")
con.close()




