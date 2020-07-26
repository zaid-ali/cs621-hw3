import os

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "students.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)
class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.Text)
        grade = db.Column(db.Integer)
        def __init__(self, name, grade):
            self.name = name
            self.grade = grade
        def __repr__(self):
            return f"Student {self.name} got a grade of {self.grade} on the midterm exam"



@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        new_student = Student(name=request.form.get("name"), grade=request.form.get("grade"))
        db.session.add(new_student)
        db.session.commit()
    return render_template("home.html")

@app.route("/delete", methods=["POST"])
def delete():
    s_id = request.form.get("ID")
    student = Student.query.get(s_id)
    db.session.delete(student)
    db.session.commit()
    return render_template("home.html")
@app.route("/allstudents", methods=["POST"])
def list_all():
    everyone=Student.query.all()
    return render_template("results.html" , students = everyone)
@app.route("/passing", methods=["POST"])
def pass_students():
    passers = Student.query.filter(Student.grade>=85)
    return render_template("results.html" , students = passers)



if __name__ == "__main__":
    app.run(debug=True)
