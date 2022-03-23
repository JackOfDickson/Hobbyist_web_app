from models.booking import Booking
from models.lesson import Lesson
from models.member import Member

import repositories.booking_repository as booking_repository
import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository


booking_repository.delete_all()
lesson_repository.delete_all()
member_repository.delete_all()


lesson1 = Lesson("Cake Baking", 8, "2022-03-29")
lesson_repository.save(lesson1)
lesson2 = Lesson("Watercolour painting", 12, "2022-03-29")
lesson_repository.save(lesson2)

member1 = Member("Carl Marks")
member_repository.save(member1)
member2 = Member("Walter White")
member_repository.save(member2)
member3 = Member("Partick Bateman")
member_repository.save(member3)
member4 = Member("Donald Duck")
member_repository.save(member4)
member5 = Member("Harry Potter")
member_repository.save(member5)
member6 = Member("Mickey Mouse")
member_repository.save(member6)
member7 = Member("Steeve Job")
member_repository.save(member7)
member8 = Member("Bill Gate")
member_repository.save(member8)

booking1 = Booking(member1, lesson1)
booking_repository.save(booking1)
booking2 = Booking(member2, lesson1)
booking_repository.save(booking2)
booking3 = Booking(member2, lesson2)
booking_repository.save(booking3)
