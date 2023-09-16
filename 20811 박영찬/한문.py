from flask import Flask, render_template, request
import os
import openai


한문 = Flask(__name__)

@한문.route('/gks.htm')
def home():
    return render_template('gks.htm')

if __name__ == '__main__':
    한문.run()