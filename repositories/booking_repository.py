from db.run_sql import run_sql
from models.booking import Booking

import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member_id, booking.lesson_id]
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
        booking = Booking(member,lesson, row['id'])
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
    
# delete individual id for extension