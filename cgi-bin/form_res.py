#!/usr/bin/env python

import sqlite3
import cgi

con = sqlite3.connect('hotel.db')

cur = con.cursor()
print("Content-type: text/html\n")
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="./add_reservation.py" method="post">
        Дата брони <input type="datetime" name="reservation_date"> 
        Дата заезда <input type="datetime" name="checkin_date">
        Дата выезда <input type="datetime" name="checkout_date">
        <label for="room_id">Номер комнаты</label>
        <select name="room_id" id="room_id">""")
cur.execute("SELECT id FROM room")
i = 0
for room_id in cur.fetchall():
    print(f"""<option value="{room_id[0]}">{room_id[0]}</option>""")
print("""</select>
        <label for="client_id">Номер клиента</label>
      <select name="client_id" id="client_id">""")
cur.execute("SELECT id FROM client")
i = 0
for client_id in cur.fetchall():
    print(f"""<option value="{client_id[0]}">{client_id[0]}</option>""")
print("""</select>
        <button type="submit">Добавить бронь</button>
    </form>
</body>
</html>""")
con.close()




