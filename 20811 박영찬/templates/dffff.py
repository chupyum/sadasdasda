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

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (username,password_hash)
        VALUES(?, ?)
    ''', (username, password_hash))
    conn.commit()
    conn.close()
    print("회원가입이 완료되었습니다.")

def login():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    a=input()
    b=input()
    cursor.execute('SELECT * FROM users WHERE username = ?', (a,))
    user = cursor.fetchone()


    conn.close()


    if user:
        if b==user[2]:
            print("성공")
            
        else:
            print("실패")
    else:
        print("User not found.")


def 비번찾기():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users')
    user = cursor.fetchall()


    conn.close()


    if user:
            print(user[0][2])

        
            
    else:
        print("실패")
비번찾기()

    

