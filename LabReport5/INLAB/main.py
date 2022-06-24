import sqlite3

conn = sqlite3.connect('chinook.db')

cursor = conn.cursor()

def select_artist():
    cursor.execute("SELECT * from artists")
    
    data = cursor.fetchall()
    for row in data:
        print(row)


def select_album():
    cursor.execute("SELECT * from albums")
    data = cursor.fetchall()

    for row in data:
        print(row)
 

print('Select:\n[1] Artists\n[2] Albums')
input = int(input("-->"))

if input == 1:
    select_artist()
elif input == 2:
    select_album()
else:
    print("invalid input")


