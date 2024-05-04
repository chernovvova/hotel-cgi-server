import sqlite3
import xml.dom.minidom

con = sqlite3.connect('hotel.db')
cur = con.cursor()

xml_file = 'new_rooms.xml'
doc = xml.dom.minidom.parse(xml_file)
rooms = doc.getElementsByTagName('record')

sql = """INSERT INTO room(room_number, type, category, cost_per_day) VALUES (?, ?, ?, ?)"""

for room in rooms:
    room_number = room.getElementsByTagName('room_number')[0].childNodes[0].data
    type = room.getElementsByTagName('type')[0].childNodes[0].data
    category = room.getElementsByTagName('category')[0].childNodes[0].data
    cost_per_day = room.getElementsByTagName('cost_per_day')[0].childNodes[0].data

    cur.execute(sql, (room_number, type, category, cost_per_day))

con.commit()
con.close()