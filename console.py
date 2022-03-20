from models.booking import Booking
from models.lesson import Lesson
from models.member import Member

import repositories.booking_repository as booking_repository
import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository


booking_repository.delete_all()
lesson_repository.delete_all()
member_repository.delete_all()


lesson1 = Lesson("Cake Baking")
lesson_repository.save(lesson1)

member1 = Member("Carl Marks")
member_repository.save(member1)

booking1 = Booking(member1, lesson1)
