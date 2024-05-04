import xml.dom.minidom
import sqlite3

con = sqlite3.connect('hotel.db')
cur = con.cursor()
doc = xml.dom.minidom.Document()

root = doc.createElement('room')
doc.appendChild(root)

rooms = cur.execute('SELECT * FROM room').fetchall()
room_fields = ['id', 'room_number', 'type', 'category', 'cost_per_day']

for row in rooms:
    record = doc.createElement('record')
    root.appendChild(record)
    for i in range(len(row)):
        element = doc.createElement(room_fields[i])
        element.appendChild(doc.createTextNode(str(row[i])))
        record.appendChild(element)

with open('room.xml', 'w') as f:
    f.write(doc.toprettyxml())

con.close()
