from flask import Flask, render_template, request
import sqlite3
from mailware import send_mail

app = Flask(__name__)

DATABASE = 'feedback.db'

def get_db():
    """Helper function to get the database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database if not already created."""
    with get_db() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer TEXT UNIQUE NOT NULL,
                        project TEXT NOT NULL,
                        rating INTEGER NOT NULL,
                        comments TEXT)''')
        conn.commit()

# Initialize the database on startup
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        project = request.form['project']
        rating = request.form['rating']
        comments = request.form['comments']

        if customer == '' or project == '':
            return render_template('index.html', message='Please enter required fields')

        # Check if the customer already exists in the database
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM feedback WHERE customer = ?', (customer,))
            result = cursor.fetchone()
            
            if result[0] == 0:
                # Insert the new feedback into the database
                cursor.execute('INSERT INTO feedback (customer, project, rating, comments) VALUES (?, ?, ?, ?)',
                               (customer, project, rating, comments))
                conn.commit()

                # Send email after submitting feedback
                send_mail(customer, project, rating, comments)

                return render_template('success.html')
            else:
                return render_template('index.html', message='You have already submitted feedback')

if __name__ == '__main__':
    app.run()

