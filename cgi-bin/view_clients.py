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
<title>Обработка книг </title>
</head>
<body>""")
print("""<table>
        <thead>
        <tr>
            <th scope="col">id</th>
            <th scope="col">firstname</th>
            <th scope="col">lastname</th>
            <th scope="col">passport</th>
        </tr>
    </thead>
    <tbody>
""")
cur.execute("SELECT * FROM client")
for client in cur.fetchall():
    print(f"<tr> <th scope=\"row\">{client[0]}</th> <td>{client[1]}</td> <td>{client[2]}</td> <td>{client[3]}</td> </tr>")
con.close()
print("""</table> </tbody> </body> </html>""")




