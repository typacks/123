import sqlite3
import datetime

def check_db():
    databaseFile = ("data.db")
    db = sqlite3.connect(databaseFile, check_same_thread=False)
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        print("DB was(1/1) found")
    except sqlite3.OperationalError:
        print("DB was(1/1) not found")
        cursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT, reg_date TEXT)")
        print("DB was(1/1) create...")

def get_now_date():
    date = datetime.datetime.today().strftime("%d.%m.%Y")
    return date

def get_users_exist(user_id):
    db = sqlite3.connect("data.db", check_same_thread=False)
    cursor = db.cursor()
    cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
        return False
    else:
        return True

def add_user_to_db(user_id):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    user = [user_id, get_now_date()]
    cursor.execute(f'''INSERT INTO users(user_id, reg_date) VALUES(?,?)''', user)
    db.commit()

def get_all_users():
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute(f"""SELECT user_id FROM users""")
    row = cursor.fetchall()
    return row