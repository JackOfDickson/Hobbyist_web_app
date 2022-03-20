from models.lesson import Lesson

import repositories.lesson_repository as lesson_repository


lesson_repository.delete_all()

lesson1 = Lesson("Cake Baking")
lesson_repository.save(lesson1)