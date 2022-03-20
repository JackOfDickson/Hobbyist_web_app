from models.lesson import Lesson
from models.member import Member


import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository


lesson_repository.delete_all()
member_repository.delete_all()


lesson1 = Lesson("Cake Baking")
lesson_repository.save(lesson1)

member1 = Member("Carl Marks")
member_repository.save(member1)