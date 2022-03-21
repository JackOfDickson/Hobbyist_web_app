from db.run_sql import run_sql
from models.lesson import Lesson

def save(lesson):
    sql = "INSERT INTO lessons (title) VALUES (%s) RETURNING id"
    values = [lesson.title]
    results = run_sql(sql, values)
    lesson.id = results[0]['id']
    return lesson

def select_all():
    lessons = []
    
    sql = "SELECT * FROM lessons"
    results = run_sql(sql)
    
    for row in results:
        lesson = Lesson(row['title'], row['id'])
        lessons.append(lesson)
    return lessons

def select(id):
    lesson = None
    
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        lesson = Lesson(result['title'], result['id'])
    return lesson

def delete_all():
    sql = "DELETE FROM lessons"
    run_sql(sql)
    
# delete individual id for extension