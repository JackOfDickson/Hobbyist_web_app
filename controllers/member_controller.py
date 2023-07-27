from flask import Flask, render_template, Blueprint, redirect, request
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

from models.member import Member
from models.lesson import Lesson
from models.booking import Booking
from app import db


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
    db.session.add(member)
    db.session.commit()
    return redirect ('/members')
    
@members_blueprint.route("/<id>/edit", methods = ['GET'])
def edit_member(id):
    member = Member.query.get(id)
    return render_template('members/edit.html', member = member)

@members_blueprint.route("/<id>", methods=['POST'])
def update_member(id):
    member = Member.query.get(id)
    member.name = request.form['name']
    db.session.commit()
    return redirect ('/members')

@members_blueprint.route("/<id>/delete")
def delete_member(id):
    member_to_delete = Member.query.get(id)
    db.session.delete(member_to_delete)
    return redirect ('/members')