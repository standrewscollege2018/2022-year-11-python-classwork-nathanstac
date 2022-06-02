import sqlite3

DATABASE = 'cars.db'

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

cursor.execute("SELECT * FROM cars")
cars = cursor.fetchall()

for car in cars:
    print(f"{car[0]} {car[1]:12} {car[3]:12}")

selection = int(input("enter number: "))
cursor.execute("SELECT * FROM cars WHERE car_id = ?", (selection,))
selected_car = cursor.fetchall()
for s in selected_car:
    print(s)

