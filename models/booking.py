from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default = uuid.uuid4)
    member_id = db.Column(UUID, db.ForeignKey("members.id"))
    lesson_id = db.Column(UUID, db.ForeignKey("lessons.id"))

    def __init__(self, member, lesson):
        self.member = member
        self.lesson = lesson