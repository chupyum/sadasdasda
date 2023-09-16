from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
import openai
import sqlite3
from flask import send_from_directory


app = Flask(__name__)
app.secret_key = 'zzz wjfEoahtvna'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def a():
    return render_template('index.html')
@app.route('/join.html', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                user TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

        username = request.form['username']
        password_hash = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO users (username,password_hash,user)
            VALUES(?, ?, ?)
        ''', (username, password_hash, username))
        conn.commit()
        conn.close()

        print("회원가입이 완료되었습니다.")
        return redirect(url_for('login'))
    return render_template('join.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    error_message = None
    wk = None
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        password = request.form['password']
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        conn.close()
        if user:
            if password==user[2]:
                if username==str('a'):
                    wk = 1
                    print(wk)
                return redirect(url_for('logined', wk = wk))
            
            else:
                print("실패")
                return redirect(url_for('logined'))
        else:
            error_message = '너 틀림 ㅋ'
    return render_template('login.html', error_message=error_message)

@app.route('/idfind.html', methods=['GET', 'POST'])
def ifind(): 
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    idfind = None
    
    if request.method == 'POST':
        password = request.form['password']
        
        cursor.execute("SELECT username FROM users WHERE password_hash = ?", (password,))
        user = cursor.fetchall()
        if user:
            idfind = '당신의 아이디는 %s 입니다' %(user[0])
        else:
            idfind = "%s을 비밀번호로 가진 아이디는 존재하지 않습니다" %(password)
    return render_template('idfind.html',idfind = idfind)
       
    
    conn.close()  # Close the database connection
    
    return render_template('idfind.html', username=username)

@app.route('/passfind.html', methods=['GET', 'POST'])
def passw(): 
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    passfind = ''
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        if user:
            passfind = '당신의 패스워드는 %s 입니다' %(user[2])
        else:
            passfind = '아이디는 존재하지 않습니다'
    conn.close()
    return render_template('passfind.html', passfind=passfind)

@app.route('/poem.html')
def poem():
    return render_template('poem.html')

@app.route('/log_out.html')
def log_out():
    return render_template('log_out.html')

@app.route('/no_move.html')
def no_move():
    return render_template('no_move.html')

@app.route('/sigma.html')
def sigma():
    return render_template('sigma.html')


@app.route('/logining.html')
def logining():
    return render_template('logining.html')

@app.route('/18.html')
def f():
    return render_template('18.html')

@app.route('/modren.html')
def modren():
    return render_template('modren.html')

@app.route('/50.html')
def h():
    return render_template('50.html')

@app.route('/1.html')
def i():
    return render_template('1.html')

@app.route('/2.html')
def j():
    return render_template('2.html')

@app.route('/study.html')
def study():
    return render_template('study.html')

@app.route('/3.html')
def k():
    return render_template('3.html')
@app.route('/assets/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/logined.html')
def logined():
    return render_template('logined.html')

@app.route('/18 - 복사본.html')
def n():
    return render_template('18 - 복사본.html')

@app.route('/18 - 복사본 (2).html')
def m():
    return render_template('18 - 복사본 (2).html')

@app.route('/18 - 복사본 (3).html')
def o():
    return render_template('/18 - 복사본 (3).html')

@app.route('/18 - 복사본 (4).html')
def p():
    return render_template('/18 - 복사본 (4).html')

@app.route('/18 - 복사본 (5).html')
def c():
    return render_template('/18 - 복사본 (5).html')
@app.route('/game.html')
def GAME():
    return render_template('/game.html')

@app.route('/18 - 복사본 (6).html')
def q():
    return render_template('/18 - 복사본 (6).html')

@app.route('/검색.html')
def r():

    return render_template('검색.html')


@app.route('/4.html')
def rl():

    return render_template('4.html')



@app.route('/execute', methods=['POST'])
def execute():
    dk = int(request.form['dk'])
    b = request.form['b']
    c = request.form['c']
    result = None

    if dk == 1:
        i = 0
        a = 0
        for i in range(int(b), int(c) + 1, 1):
            a = a + i
        num=a
        k = []
        digit_count = len(str(num))
        dia = len(str(num))

        while digit_count > 4:
            o = 4
            print(num)
            j = num % 10**o  

            k.append(j)
            digit_count = digit_count - 4
            print(k)
            print(j)
            num = num // 10**o  
            print(num)

        if(digit_count<=4):
            k.append(num)
            print(k)
        s=int(dia/4)
        ui=dia/4
        print(ui)
        if(ui<=1):
            result = "%d"%(k[0])
        if(ui>1 and ui<=2):
            result = "%d만%d"%(k[1],k[0])
        if(ui>2 and ui<=3):
            result = "%d억%d만%d"%(k[s],k[1],k[0])
        if(ui>3 and ui<=4):
            result = "%d조%d억%d만%d" %(k[3],k[2],k[1],k[0])
        if(ui>4 and ui<=5):
            result = "%d경%d조%d억%d만%d"%(k[4],k[3],k[2],k[1],k[0])
        if(ui>5 and ui<=6):
            result = "%d해%d경%d조%d억%d만%d"%(k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>6 and ui<=7):
            result = "%d자%d해%d경%d조%d억%d만%d"%(k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>7 and ui<=8):
            result = "%d양%d자%d해%d경%d조%d억%d만%d"%(k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>8 and ui<=9):
            result = "%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>9 and ui<=10):
            result = "%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>10 and ui<=11):
            result = "%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>11 and ui<=12):
            result = "%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k,[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>12 and ui<=13):
            result = "%d재%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[12],k[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>13 and ui<=14):
            result = "%d극%d재%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[13],k[12],k[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])


    elif dk == 2:
        i = 0
        a = 0
        for i in range(int(b), int(c) + 1, 1):
            a = i ** 2 + a
        
        num=a
        k = []
        digit_count = len(str(num))
        dia = len(str(num))

        while digit_count > 4:
            o = 4
            print(num)
            j = num % 10**o  

            k.append(j)
            digit_count = digit_count - 4
            print(k)
            print(j)
            num = num // 10**o  
            print(num)

        if(digit_count<=4):
            k.append(num)
            print(k)
        s=int(dia/4)
        ui=dia/4
        print(ui)
        if(ui<=1):
            result = "%d"%(k[0])
        if(ui>1 and ui<=2):
            result = "%d만%d"%(k[1],k[0])
        if(ui>2 and ui<=3):
            result = "%d억%d만%d"%(k[s],k[1],k[0])
        if(ui>3 and ui<=4):
            result = "%d조%d억%d만%d" %(k[3],k[2],k[1],k[0])
        if(ui>4 and ui<=5):
            result = "%d경%d조%d억%d만%d"%(k[4],k[3],k[2],k[1],k[0])
        if(ui>5 and ui<=6):
            result = "%d해%d경%d조%d억%d만%d"%(k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>6 and ui<=7):
            result = "%d자%d해%d경%d조%d억%d만%d"%(k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>7 and ui<=8):
            result = "%d양%d자%d해%d경%d조%d억%d만%d"%(k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>8 and ui<=9):
            result = "%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>9 and ui<=10):
            result = "%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>10 and ui<=11):
            result = "%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>11 and ui<=12):
            result = "%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k,[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>12 and ui<=13):
            result = "%d재%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[12],k[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>13 and ui<=14):
            result = "%d극%d재%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[13],k[12],k[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])

    elif dk == 3:
        i = 0
        a = 0
        for i in range(int(b), int(c) + 1, 1):
            a = i ** 3 + a
        num=a
        k = []
        digit_count = len(str(num))
        dia = len(str(num))

        while digit_count > 4:
            o = 4
            print(num)
            j = num % 10**o  

            k.append(j)
            digit_count = digit_count - 4
            print(k)
            print(j)
            num = num // 10**o  
            print(num)

        if(digit_count<=4):
            k.append(num)
            print(k)
        s=int(dia/4)
        ui=dia/4
        print(ui)
        if(ui<=1):
            result = "%d"%(k[0])
        if(ui>1 and ui<=2):
            result = "%d만%d"%(k[1],k[0])
        if(ui>2 and ui<=3):
            result = "%d억%d만%d"%(k[s],k[1],k[0])
        if(ui>3 and ui<=4):
            result = "%d조%d억%d만%d" %(k[3],k[2],k[1],k[0])
        if(ui>4 and ui<=5):
            result = "%d경%d조%d억%d만%d"%(k[4],k[3],k[2],k[1],k[0])
        if(ui>5 and ui<=6):
            result = "%d해%d경%d조%d억%d만%d"%(k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>6 and ui<=7):
            result = "%d자%d해%d경%d조%d억%d만%d"%(k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>7 and ui<=8):
            result = "%d양%d자%d해%d경%d조%d억%d만%d"%(k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>8 and ui<=9):
            result = "%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>9 and ui<=10):
            result = "%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>10 and ui<=11):
            result = "%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>11 and ui<=12):
            result = "%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k,[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>12 and ui<=13):
            result = "%d재%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[12],k[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>13 and ui<=14):
            result = "%d극%d재%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[13],k[12],k[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
    else:
        result = "다시 입력해주세요"

    return render_template('result.html', result=result)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)

