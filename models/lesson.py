from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Lesson(db.Model):
    __tablename__ = "lessons"
    
    id = db.Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
    title = db.Column(db.String(64))
    capacity = db.Column(db.Integer())
    lesson_date = db.Column(db.String(64))
    bookings = db.relationship('Booking', backref="lesson")


    def __init__(self, title, capacity, lesson_date, id = None):
        self.title = title
        self.capacity = capacity
        self.lesson_date = lesson_date
        self.id = id