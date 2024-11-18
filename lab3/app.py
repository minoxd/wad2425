import math

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentman.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    class_name = db.Column(db.String(50))
    mark = db.Column(db.Integer)


@app.route('/add')
def add_student():
    from flask import request
    name, class_name, mark = request.args.get('name'), request.args.get('class_name'), request.args.get('mark')
    if name and class_name and mark:
        student = Student(name=name, class_name=class_name, mark=mark)
        db.session.add(student)
        db.session.commit()
        return 'added'
    return 'error'


@app.route('/update')
def update_student():
    students = Student.query.filter(Student.mark < 60).all()
    for student in students:
        student.class_name = 'Two'
    students = Student.query.filter(Student.mark >= 60).all()
    for student in students:
        student.class_name = 'One'
    db.session.commit()
    return 'updated'


@app.route('/get')
def get_student():
    excellent = Student.query.filter(Student.mark > 75).all()
    good = Student.query.filter(Student.mark <= 75, Student.mark >= 60).all()
    average = Student.query.filter(Student.mark < 60).all()
    return render_template('students.html', excellent=excellent, good=good, average=average)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/welcome')
def welcome():
    return 'Welcome to Flask Development!<br>This is Labwork 3: Flask/MySQL/API'


@app.route('/table')
def table():
    data = [
        {'name': 'John', 'age': 25},
        {'name': 'Michael', 'age': 26},
        {'name': 'Alice', 'age': 27},
        {'name': 'Bob', 'age': 28},
        {'name': 'Jim', 'age': 29},
    ]
    return render_template('table.html', students=data)


@app.route('/factorial/<int:n>')
def factorial(n):
    def f(n):
        if n == 0:
            return 1
        return n * f(n - 1)

    return 'result = ' + str(f(n))


@app.route('/factorial2/<int:n>')
def factorial2(n):
    return f'result = {math.factorial(n)}'
@app.route('/factorial3/<int:n>')
def factorial3(n):
    return str(math.factorial(n))


@app.route('/is-prime/<int:n>')
def is_prime(n):
    if n < 2:
        return str(False)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return str(False)
    return str(True)


@app.route('/sort')
def sort():
    from flask import request
    arr = request.args.get('arr')
    if arr:
        arr = list(map(int, arr.split(',')))
        arr = sorted(arr)
        return f'sorted: {arr}'
    return 'invalid'


@app.route('/reverse/<string:s>')
def reverse(s):
    return s[::-1]


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
