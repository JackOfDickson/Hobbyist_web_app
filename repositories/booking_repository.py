from db.run_sql import run_sql
from models.booking import Booking

import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository

# def check_duplicate_booking(booking):
#     member = booking.member
#     lesson_members = lesson_repository.members(booking.lesson)
#     for lesson_member in lesson_members:
#         if member == lesson_member:
#             return True
#         else: continue
#     return False

def check_capacity(booking):
    lesson = booking.lesson
    number_signed_up = len(lesson_repository.members(lesson))
    if lesson.capacity > number_signed_up:
        return False
    else:
        return True

def save(booking):
    # is_duplicate = check_capacity(booking)
    # if is_duplicate == True:
    #     return "error, duplicate bookings are not allowed!!!"
    is_full = check_capacity(booking)
    if is_full == True:
        return "error, room is full!!!"
    
    sql = "INSERT INTO bookings (member_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.lesson.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

def select_all():
    bookings = []
    
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    
    for row in results:
        member = member_repository.select(row['member_id'])
        lesson = lesson_repository.select(row['lesson_id'])
        booking = Booking(member, lesson, row['id'])
        bookings.append(booking)
    return bookings

def select(id):
    booking = None
    
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        booking = booking(result['member_id'], result['lesson_id'], result['id'])
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)