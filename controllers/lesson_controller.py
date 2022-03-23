from flask import Flask, render_template, Blueprint, redirect, request
import repositories.lesson_repository as lesson_repository
from models.lesson import Lesson

lessons_blueprint = Blueprint("lessons", __name__)

@lessons_blueprint.route("/lessons")
def lessons():
    lessons = lesson_repository.select_all()
    return render_template("lessons/index.html", lessons = lessons)

@lessons_blueprint.route("/lessons/<id>")
def show(id):
    lesson = lesson_repository.select(id)
    members = lesson_repository.members(lesson)
    return render_template("/lessons/show.html", lesson = lesson, members = members)

@lessons_blueprint.route("/lessons/new", methods = ['GET'])
def new_member():
    return render_template ('lessons/new.html')

@lessons_blueprint.route("/lessons", methods=['POST'])
def create_lesson():
    title = request.form['title']
    capacity = request.form['capacity']
    lesson_date = request.form['lesson_date']
    lesson = Lesson(title, capacity, lesson_date)
    lesson_repository.save(lesson)
    return redirect ('/lessons')

@lessons_blueprint.route("/lessons/<id>/edit", methods = ['GET'])
def edit_lesson(id):
    lesson = lesson_repository.select(id)
    return render_template('lessons/edit.html', lesson = lesson)

@lessons_blueprint.route("/lessons/<id>", methods=['POST'])
def update_lesson(id):
    title = request.form['title']
    lesson = Lesson(title, id)
    lesson_repository.update(lesson)
    return redirect ('/lessons')

@lessons_blueprint.route("/lessons/<id>/delete")
def delete_lesson(id):
    lesson_repository.delete(id)
    return redirect ('/lessons')
