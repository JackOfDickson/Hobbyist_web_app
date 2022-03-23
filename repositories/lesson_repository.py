from db.run_sql import run_sql
from models.lesson import Lesson
from models.member import Member

def save(lesson):
    sql = "INSERT INTO lessons (title, capacity, lesson_date) VALUES (%s, %s, %s) RETURNING id"
    values = [lesson.title, lesson.capacity, lesson.lesson_date]
    results = run_sql(sql, values)
    lesson.id = results[0]['id']
    return lesson

def select_all():
    lessons = []
    
    sql = "SELECT * FROM lessons"
    results = run_sql(sql)
    
    for row in results:
        lesson = Lesson(row['title'], row['capacity'],row['lesson_date'], row['id'])
        lessons.append(lesson)
    return lessons

def select(id):
    lesson = None
    
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        lesson = Lesson(result['title'], result['capacity'], result['lesson_date'], result['id'])
    return lesson

def delete_all():
    sql = "DELETE FROM lessons"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE FROM lessons WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def members(lesson):
    members = []
    
    sql = 'SELECT * FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE lesson_id = %s'
    values = [lesson.id]
    results = run_sql(sql, values)
    
    for row in results:
        member = Member(row['name'], row['member_id'])
        members.append(member)
    return members

def update(lesson):
    sql = "UPDATE lessons SET (title, capacity, lesson_date) = (%s, %s, %s) WHERE id = %s"
    values = [lesson.title, lesson.capacity, lesson.lesson_date, lesson.id]
    run_sql(sql, values)