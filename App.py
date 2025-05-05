from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('students.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = get_db_connection()
        conn.execute('INSERT INTO students (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        conn.close()
        return redirect(url_for('students'))
    return render_template('add_student.html')

@app.route('/student/<int:id>')
def student_detail(id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('student_detail.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
