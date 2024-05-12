import sqlite3

con = sqlite3.connect("hotel.db")

cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS client(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname VARCHAR(30) NOT NULL,
                lastname VARCHAR(30) NOT NULL,
                passport VARCHAR(20) NOT NULL UNIQUE
            );""")

cur.execute("""CREATE TABLE IF NOT EXISTS room(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                room_number INTEGER NOT NULL UNIQUE,
                type TEXT NOT NULL,
                category TEXT NOT NULL,
                cost_per_day INTEGER NOT NULL
            );""")

cur.execute("""CREATE TABLE IF NOT EXISTS reservation(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reservation_date TEXT NOT NULL,
                checkin_date TEXT NOT NULL,
                checkout_date TEXT NOT NULL,
                room_id INTEGER NOT NULL,
                client_id INTEGER NOT NULL,
                FOREIGN KEY (room_id) REFERENCES room(id),
                FOREIGN KEY (room_id) REFERENCES client(id)
         );""")

cur.execute("""CREATE TABLE IF NOT EXISTS bill(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reservation_id INTEGER NOT NULL,
                total_price INTEGER,
                FOREIGN KEY (reservation_id) REFERENCES reservation(id)
        );""")

room_list = [
    (101, "single", "standart", 1000),
    (102, "double", "standart", 1500),
    (103, "single", "superior", 3000),
    (104, "twin", "standart", 1600),
    (105, "triple", "superior", 4000),
    (201, "twin", "deluxe", 4000),
    (202, "twin", "deluxe", 4000),
    (203, "family", "standart", 4200),
    (204, "family", "superior", 4500),
    (301, "twin", "deluxe", 4000)
]

client_list = [
    ("Ivan", "Ivanov", 1234567890),
    ("Petr", "Petrov", 5352954893),
    ("Ivan", "Petrov", 3291583034),
    ("Petr", "Ivanov", 4859378591),
    ("Vasia", "Pypkin", 3895472894),
    ("Egor", "Egorov", 3485940210),
    ("Vlad", "Egorov", 1003829043),
]

reservation_list = [
    ('18-04-2024', '21-04-2024', '28-04-2024', 5, 1),
    ('19-04-2024', '25-04-2024', '1-05-2024', 1, 2),
    ('25-03-2024', '24-04-2024', '30-04-2024', 10, 3),
    ('15-04-2024', '23-04-2024', '5-05-2024', 3, 5),
    ('16-04-2024', '18-04-2024', '23-04-2024', 4, 6)
]

bill_list = [
    (1, 28000),
    (2, 7000),
    (3, 24000),
    (4, 36000),
    (5, 8000)
]

insert_room = """INSERT INTO room(room_number, type, category, cost_per_day) VALUES (?, ?, ?, ?)"""
insert_client = """INSERT INTO client(firstname, lastname, passport) VALUES (?, ?, ?)"""
insert_reservation = """INSERT INTO reservation(reservation_date, checkin_date, checkout_date, room_id, client_id) VALUES (?, ?, ?, ?, ?)"""
insert_bill = """INSERT INTO bill(reservation_id, total_price) VALUES (?, ?)"""
con.executemany(insert_room, room_list)
con.executemany(insert_client, client_list)
con.executemany(insert_reservation, reservation_list)
con.executemany(insert_bill, bill_list)

"""
type:
Single room — номер с односпальной кроватью
Double room — номер с двуспальной кроватью
Twin room — номер с двумя кроватями
Triple room — номер с тремя кроватями
Family room — семейный номер (как правило, с тремя и более кроватями)

category:
Standard room — стандартный номер
Superior room — номер повышенного комфорта
Suite / Deluxe room — номер «люкс»
"""
con.commit()
con.close()
