from models.booking import Booking
from models.lesson import Lesson
from models.member import Member
from app import db
from flask.cli import with_appcontext
import click


@click.command('seed')
@with_appcontext
def seed():
    lesson1 = Lesson("Cake Baking", 8, "2022-03-29")
    lesson2 = Lesson("Watercolour painting", 12, "2022-03-29")

    # db.session.add(lesson1)
    # db.session.add(lesson2)

    member1 = Member("Carl Marks")
    member2 = Member("Walter White")
    member3 = Member("Partick Bateman")
    member4 = Member("Donald Duck")
    member5 = Member("Harry Potter")
    member6 = Member("Mickey Mouse")
    member7 = Member("Steeve Job")
    member8 = Member("Bill Gate")

    db.session.add_all([
        lesson1, lesson2, 
        member1, member2, member3, member4, member5, member6, member7, member8
        ])

    booking1 = Booking(member1, lesson1)
    booking2 = Booking(member2, lesson1)
    booking3 = Booking(member2, lesson2)

    db.session.add_all([booking1, booking2, booking3])

    db.session.commit()
