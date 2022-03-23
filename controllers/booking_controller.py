from flask import Flask, render_template, Blueprint, redirect, request
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route('/bookings')
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)

@bookings_blueprint.route('/bookings/new', methods = ['GET'])
def new_booking():
    members = member_repository.select_all()
    lessons = lesson_repository.select_all()
    return render_template("bookings/new.html", members = members, lessons = lessons)

@bookings_blueprint.route('/bookings', methods = ['POST'])
def create_booking():
    member_id = request.form['member_id']
    lesson_id = request.form['lesson_id']
    member = member_repository.select(member_id)
    lesson = lesson_repository.select(lesson_id)
    booking = Booking(member,lesson)
    booking_repository.save(booking)
    return redirect('/bookings')

@bookings_blueprint.route('/bookings/<id>/delete')
def delete_booking(id):
    booking_repository.delete(id)
    return redirect('/bookings')