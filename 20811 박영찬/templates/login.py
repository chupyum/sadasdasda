from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # 보안을 위한 시크릿 키 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite 데이터베이스 경로 설정
d = SQLAlchemy(app)

class Users(SQLAlchemy(app).Model):
    id = d.column(d.Integer,primary_key=True)
    nickname = db.column(d.string(20),unique=True, nullable=False)
    email = db.column(d.string(20),unique=True, nullable=False)
    password = db.column(d.string(100),unique=True, nullable=False)

class signup(FlaskForm):
    nickname = StringField('아이디',validators=[DataRequired()])
    email = StringField('이메일',validators=[DataRequired(),Email()])
    password = PasswordField('비밀번호')
    checking = PasswordField('비밀 번호 확인')
    submit = SubmitField('Sign Up')
