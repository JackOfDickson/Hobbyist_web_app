from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Member(db.Model):
    __tablename__ = "members"

    id = db.Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
    name = db.Column(db.String(64))
    bookings = db.relationship('Booking', backref="member")

    def __init__(self, name, id = None):
        self.name = name
        self.id = id
        