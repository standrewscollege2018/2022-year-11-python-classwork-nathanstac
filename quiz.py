import sqlite3

DATABASE = 'quiz.db.db'

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

print("welcome to the quizes")
print("quiz cars or quiz mtb")
print("which quiz do you want to do")
reply = input()
if reply == "cars":
    print("quiz cars")
elif reply == "mtb":
    print("quiz mtb")

cursor.execute("SELECT * FROM answers")
quizes = cursor.fetchall()

for quiz in quizes:
    print(f"{quiz[0]}")
