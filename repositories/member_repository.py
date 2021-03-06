from db.run_sql import run_sql
from models.member import Member
from models.lesson import Lesson

def save(member):
    sql = "INSERT INTO members (name) VALUES (%s) RETURNING id"
    values = [member.name]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    members = []
    
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    
    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        member = Member(result['name'], result['id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def lessons(member):
    lessons = []
    
    sql = 'SELECT * FROM lessons INNER JOIN bookings ON bookings.lesson_id = lessons.id WHERE member_id = %s'
    values = [member.id]
    results = run_sql(sql, values)
    
    for row in results:
        lesson = Lesson(row['title'], row['capacity'],row['lesson_date'] , row['lesson_id'])
        lessons.append(lesson)
    return lessons
    
def update(member):
    sql = "UPDATE members SET name = %s WHERE id = %s"
    values = [member.name, member.id]
    run_sql(sql, values)