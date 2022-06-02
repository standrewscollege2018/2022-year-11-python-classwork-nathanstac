# Write your code here :-)
import sqlite3

DATABASE = 'titanic.db'

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

cursor.execute("SELECT * FROM passenger")
passengers = cursor.fetchall()

for passenger in passengers:
    print(f"{passenger[0]} {passenger[1]:12} {passenger[3]:12}")

selection = int(input("enter number: "))
cursor.execute("SELECT * FROM passenger WHERE passenger_id = ?", (selection,))
selected_passenger = cursor.fetchall()
for s in selected_passenger:
    print(s)
