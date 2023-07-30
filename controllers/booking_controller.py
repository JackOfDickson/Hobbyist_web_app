from flask import Flask, render_template, Blueprint, redirect, request
from models.booking import Booking
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
    members_booked_for_lesson = Member.query.join(Booking).filter(Booking.lesson_id == lesson.id)
    for booked_member in members_booked_for_lesson:
        if member.id == (booked_member.id):
            print("already booked")
            return redirect('/bookings')
    if members_booked_for_lesson.count() >= lesson.capacity:
        print("Class is full")
        return redirect('/bookings')
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