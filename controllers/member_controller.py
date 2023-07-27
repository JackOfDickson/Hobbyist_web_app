from flask import Flask, render_template, Blueprint, redirect, request
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

from models.member import Member
from models.lesson import Lesson
from models.booking import Booking


members_blueprint = Blueprint("members", __name__, url_prefix="/members")

@members_blueprint.route("")
def members():
    members = Member.query.all()
    return render_template("members/index.html", members = members)

@members_blueprint.route("/<id>")
def show(id):
    member = Member.query.get(id)
    lessons = Lesson.query.join(Booking).filter(Booking.member_id == id)
    return render_template("/members/show.html", lessons = lessons, member = member)

@members_blueprint.route("/new", methods = ['GET'])
def new_member():
    return render_template ('members/new.html')

@members_blueprint.route("", methods=['POST'])
def create_member():
    name = request.form['name']
    member = Member(name)
    member_repository.save(member)
    return redirect ('/members')
    
@members_blueprint.route("/<id>/edit", methods = ['GET'])
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member = member)

@members_blueprint.route("/<id>", methods=['POST'])
def update_member(id):
    name = request.form['name']
    member = Member(name, id)
    member_repository.update(member)
    return redirect ('/members')

@members_blueprint.route("/<id>/delete")
def delete_member(id):
    member_repository.delete(id)
    return redirect ('/members')