#!/usr/bin/env python

import sqlite3
import cgi

form = cgi.FieldStorage()
firstname = form.getfirst("firstname", "не задано")
lastname = form.getfirst("lastname", "не задано")
passport = form.getfirst("passport", "не задано")
con = sqlite3.connect('hotel.db')

cur = con.cursor()
sql = "INSERT INTO client(firstname, lastname, passport) VALUES (?, ?, ?)"
cur.execute(sql, (firstname, lastname, passport))
con.commit()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="UTF-8">
<title>Обработка книг </title>
</head>
<body>""")
print("<h1>Клиенты: </h1>\n")

cur.execute("SELECT * FROM client")
for client in cur.fetchall():
    print(f"<p>{client[0]}  {client[1]}  {client[2]}</p>\n")
con.close()
print("""</body> </html>""")




