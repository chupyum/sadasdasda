import sqlite3
def create():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(username, password_hash):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (username,password_hash)
        VALUES(?, ?)
    ''', (username, password_hash))
    conn.commit()
    conn.close()

def signup():
    username = input("사용자 이름: ")
    password_hash = input("비밀번호: ")

    insert_user(username, password_hash)
    print("회원가입이 완료되었습니다.")
def login():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    a=input("닉네임:")
    username_to_search = a
    b=input("비번:")
    cursor.execute('SELECT * FROM users WHERE username = ?', (username_to_search,))
    user = cursor.fetchone()


    conn.close()

    if user:
        if b==user[2]:
            print("성공")
        else:
            print("실패")
    else:
        print("User not found.")



login()
