import sqlite3

DATABASE = "database.db"


def database():
    global conn, cursor
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `config` (config_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, company_name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()
    cursor.execute("SELECT * from config WHERE config_id = 1")
    if cursor.fetchone() is None:
        pass
    else:
        cursor.execute('INSERT INTO config (company_name) VALUES ("test")')


database()
print("Insert Company name")
name = raw_input()
cursor.execute("UPDATE config SET company_name = ? WHERE config_id = 1", (name,))
conn.commit()