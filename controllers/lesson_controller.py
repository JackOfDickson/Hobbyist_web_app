from flask import Flask, render_template, Blueprint, redirect, request
import repositories.lesson_repository as lesson_repository

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