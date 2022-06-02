
# Write your code here :-)
import sqlite3

DATABASE = 'cars.db'

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

cursor.execute("SELECT * FROM cars")
cars = cursor.fetchall()
print(f"{'Plate':10}")
print("="*160)
for car in cars:
    print(f"{car[1]:10} {car[2]:20} {car[3]:20} {car[4]:20} {car[5]:10}")


cursor.execute("SELECT number_plate, driver FROM cars WHERE driver = tom gibson")
cars = cursor.fetchall()
print(f"{'Plate':10}")
print("="*160)
for car in cars:
    print(f"{car[0]:10} {car[1]:20}")


