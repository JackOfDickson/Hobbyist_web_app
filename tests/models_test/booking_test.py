import unittest
from models.booking import Booking
from models.member import Member
from models.lesson import Lesson

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.lesson1 = Lesson("Cake Baking", 8, "2022-03-09")
        self.member1 = Member("Carl Marx")
        self.booking1 = Booking(self.member1, self.lesson1)
        
    def test_id_is_none(self):
        self.assertEqual(1, self.booking1.id)
    
    def test_booking_has_member(self):
        self.assertEqual(self.member1, self.booking1.member)
        
    def test_booking_has_lessons(self):
        self.assertEqual(self.lesson1, self.booking1.lesson)