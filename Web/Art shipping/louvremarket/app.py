from flask import Flask, request, render_template
from contextlib import closing
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('contacts.db')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        submit(email, message)
    return render_template('index.html')

def submit(email, message):
    with closing(sqlite3.connect('contacts.db')) as conn:
        with closing(conn.cursor()) as cursor:
            request = f"INSERT INTO messages (email, message) VALUES ('{email}', '{message}')"
            cursor.execute(request)
        conn.commit()
        conn.close()

@app.route('/secret', methods=['GET'])
def secret_zone():
    return render_template('secret.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10040)
