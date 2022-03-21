from flask import Flask, render_template, Blueprint, redirect, request
import repositories.member_repository as member_repository

from models.member import Member


members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    lessons = member_repository.lessons(member)
    return render_template("/members/show.html", lessons = lessons, member = member)

@members_blueprint.route("/members/new", methods = ['GET'])
def new_member():
    return render_template ('members/new.html')

@members_blueprint.route("/members", methods=['POST'])
def create_member():
    name = request.form['name']
    member = Member(name)
    member_repository.save(member)
    return redirect ('/members')
    
# @members_blueprint.route("/members/<id>",)