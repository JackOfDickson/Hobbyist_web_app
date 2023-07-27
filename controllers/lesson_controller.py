from flask import Flask, render_template, Blueprint, redirect, request
from repositories.booking_repository import check_capacity
import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository
from models.lesson import Lesson
from models.member import Member
from models.booking import Booking
from app import db

lessons_blueprint = Blueprint("lessons", __name__, url_prefix="/lessons")

@lessons_blueprint.route("")
def lessons():
    lessons = Lesson.query.all()
    return render_template("lessons/index.html", lessons = lessons)

@lessons_blueprint.route("/<id>")
def show(id):
    lesson = Lesson.query.get(id)
    members = Member.query.join(Booking).filter("lesson_id" == id)
    return render_template("/lessons/show.html", lesson = lesson, members = members)

@lessons_blueprint.route("/new", methods = ['GET'])
def new_member():
    return render_template ('lessons/new.html')

@lessons_blueprint.route("/", methods=['POST'])
def create_lesson():
    title = request.form['title']
    capacity = request.form['capacity']
    lesson_date = request.form['lesson_date']
    lesson = Lesson(title, capacity, lesson_date)
    db.session.add(lesson)
    db.session.commit()
    return redirect ('/lessons')

@lessons_blueprint.route("/<id>/edit", methods = ['GET'])
def edit_lesson(id):
    lesson = Lesson.query.get(id)
    return render_template('lessons/edit.html', lesson = lesson)

@lessons_blueprint.route("/<id>", methods=['POST'])
def update_lesson(id):
    lesson = Lesson.query.get(id)
    lesson.title = request.form['title']
    lesson.capacity = request.form['capacity']
    lesson.lesson_date = request.form['lesson_date']
    db.session.commit()
    return redirect ('/lessons')

@lessons_blueprint.route("/<id>/delete")
def delete_lesson(id):
    lesson_to_delete = Lesson.query.get(id)
    db.session.delete(lesson_to_delete)
    db.session.commit()
    return redirect ('/lessons')
