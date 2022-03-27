import unittest
import repositories.booking_repository as booking_repository
from models.booking import Booking
from models.member import Member
from models.lesson import Lesson

class TestBookingRepository(unittest.TestCase):
    
    def setUp(self):
        self.lesson1 = Lesson("Cake Baking", 2, "2022-03-09")
        self.member1 = Member("Carl Marx")
        self.member2 = Member("Bill Gate")
        self.member3 = Member("Patric Bateman")
        self.booking1 = Booking(self.member1, self.lesson1)