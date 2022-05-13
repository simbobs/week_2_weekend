import unittest

from src.caraoke import Caraoke
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestCaraoke(unittest.TestCase):
    def setUp(self):
        self.caraoke = Caraoke("Cosmo")
        
        self.room1 = Room("Sashay", 5, 3.00)
        self.room2 = Room("Cher", 3, 5.00)
        
        self.guest1 = Guest("Simona", 50.00)
        self.guest2 = Guest("Lorena", 100.00)
        self.guest3 = Guest("Paula", 70.00)
        
    def test_caraoke_can_add_rooms(self):
        self.caraoke.add_room(self.room1)
        self.assertEqual(1, len(self.caraoke._rooms))
    
    def test_can_find_rooms_in_caraoke(self):
         self.caraoke.add_room(self.room1)
         self.caraoke.add_room(self.room2)
         self.caraoke.find_room(self.room2)
         self.assertEqual(self.room2, self.caraoke.find_room(self.room2))
         self.assertEqual("Cher", self.caraoke.find_room(self.room2).name)
         
    
    def test_caraoke_can_collect_entry_fee(self):
        self.caraoke.add_room(self.room1)
        self.caraoke.collect_entry_fee(self.room1)
        self.assertEqual(3.00, self.caraoke._till_total)

    
    def test_can_check_in_customer_if_room_has_space(self):
        self.caraoke.add_room(self.room1)
        self.room1.add_guest(self.guest1)
        self.caraoke.check_in_guest(self.guest2, self.room1)
        self.assertEqual(2, self.room1.count_guests())
        self.assertEqual(3, self.caraoke._till_total)
        self.assertEqual(97, self.guest2.wallet)
        self.assertEqual("Lorena", self.caraoke._rooms[0]._guests[1].name)
        
        
    def test_cant_check_in_customer_if_room_is_at_capacity(self):
        guest4 = Guest("Massimo", 30.00)
       
        self.caraoke.check_in_guest(self.guest1, self.room2)
        self.caraoke.check_in_guest(self.guest2, self.room2)
        self.caraoke.check_in_guest(self.guest3, self.room2)
        self.caraoke.check_in_guest(guest4, self.room2)
        self.assertEqual(3, self.room2.count_guests())
        self.assertEqual(30.00, guest4.wallet)
        self.assertEqual(15, self.caraoke._till_total)
    
    
    def test_can_check_out_customer(self):
        self.caraoke.add_room(self.room1)
        self.caraoke.check_in_guest(self.guest1, self.room1)
        self.caraoke.check_in_guest(self.guest2, self.room1)
        self.caraoke.check_out_guest(self.guest1, self.room1)
        self.assertEqual("Lorena", self.room1._guests[0].name)
        self.assertEqual(1, len(self.room1._guests))
