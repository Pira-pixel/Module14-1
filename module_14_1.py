import sqlite3

# Создание подключения к базе данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы Users, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Удаление всех записей из таблицы Users
cursor.execute('DELETE FROM Users')

# Заполнение таблицы 10 записями
for i in range(10):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User {i + 1}', f'example{i + 1}@gmail.com', (i + 1) * 10, 1000))

# Обновление balance у каждой 2-й записи начиная с 1-й на 500
for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User {i}'))

# Удаление каждой 3-й записи в таблице начиная с 1-й
for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User {i}',))

# Выборка всех записей, где возраст не равен 60
cursor.execute('SELECT * FROM Users WHERE age != 60')
result = cursor.fetchall()

# Вывод результатов в консоль
for user in result:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()
