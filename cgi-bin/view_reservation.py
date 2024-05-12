#!/usr/bin/env python

import sqlite3
import cgi

con = sqlite3.connect('hotel.db')

cur = con.cursor()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="UTF-8">
<title>Бронь </title>
</head>
<body>""")
print("""<table>
        <thead>
        <tr>
            <th scope="col">id</th>
            <th scope="col">reservation_date</th>
            <th scope="col">checkin_date</th>
            <th scope="col">checkout_date</th>
            <th scope="col">room_id</th>
            <th scope="col">client_id</th>
        </tr>
    </thead>
    <tbody>
""")

cur.execute("SELECT * FROM reservation")
for reseravation in cur.fetchall():
    print(f"""<tr> 
                <th scope=\"row\">{reseravation[0]}</th> 
                <td>{reseravation[1]}</td> 
                <td>{reseravation[2]}</td> 
                <td>{reseravation[3]}</td>
                <td>{reseravation[4]}</td>
                <td>{reseravation[5]}</td> 
            </tr>""")
con.close()
print("""</table> </tbody> </body> </html>""")




