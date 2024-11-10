import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)  
''')

#Заполните её 10 записями:
#for i in range(1, 11):
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", i*10, 1000))

#Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# i=-1
# while i < 10:
#     i+=2
#     cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))

#Удалите каждую 3ую запись в таблице начиная с 1ой:
# i=-2
# while i < 10:
#     i+=3
#     cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))

#Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль
#Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>

#выборка для имени пользователя
cursor.execute("SELECT username FROM Users WHERE age != ?", (60, ))
users1 = cursor.fetchall()
list_name = []
for i in users1:
    i = list(i)
    list_name.append(" ".join(i))

#выборка для возраста пользователя
cursor.execute("SELECT age FROM Users WHERE age != ?", (60, ))
users2 = cursor.fetchall()
list_age = []
for i in users2:
    for n in i:
        list_age.append(n)

#выборка для баланса пользователя
cursor.execute("SELECT balance FROM Users WHERE age != ?", (60, ))
users3 = cursor.fetchall()
list_balance = []
for i in users3:
    for n in i:
        list_balance.append(n)

#выборка для эл.почты пользователя
cursor.execute("SELECT email FROM Users WHERE age != ?", (60, ))
users4 = cursor.fetchall()
list_email = []
for i in users4:
    i = list(i)
    list_email.append(" ".join(i))

#формирование вывода в виде f-строки по заданным критериям
for index in range(len(list_name)):
    username = list_name[index]
    email = list_email[index]
    age = list_age[index]
    balance = list_balance[index]
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

connection.commit()
connection.close()