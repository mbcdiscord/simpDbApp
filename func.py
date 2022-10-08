import sqlite3

# conn = sqlite3.connect("main.db")
# cursor = conn.execute('SELECT * FROM animals WHERE id = 1')

# row = cursor.fetchone()
# print(row[1])


def main(n):

    conn = sqlite3.connect("main.db")
    cursor = conn.execute('SELECT * FROM animals WHERE id = ?', (n.get(),))
    row = cursor.fetchone()
    return row[1]
