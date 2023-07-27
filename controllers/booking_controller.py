from flask import Flask, render_template, Blueprint, redirect, request
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository
from models.lesson import Lesson
from models.member import Member
from app import db

bookings_blueprint = Blueprint("bookings", __name__, url_prefix="/bookings")

@bookings_blueprint.route('')
def bookings():
    bookings = Booking.query.all()
    return render_template("bookings/index.html", bookings = bookings)

@bookings_blueprint.route('/new', methods = ['GET'])
def new_booking():
    members = Member.query.all()
    lessons = Lesson.query.all()
    return render_template("bookings/new.html", members = members, lessons = lessons)

@bookings_blueprint.route('/', methods = ['POST'])
def create_booking():
    member_id = request.form['member_id']
    lesson_id = request.form['lesson_id']
    member = Member.query.get(member_id)
    lesson = Lesson.query.get(lesson_id)
    booking = Booking(member,lesson)
    db.session.add(booking)
    db.session.commit()
    return redirect('/bookings')

@bookings_blueprint.route('/<id>/delete')
def delete_booking(id):
    booking_to_delete = Booking.query.get(id)
    db.session.delete(booking_to_delete)
    db.session.commit()
    return redirect('/bookings')