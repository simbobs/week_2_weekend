import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Simona", 50.00)
        self.room = Room("Sashay", 5, 3.00)
        
    def test_guest_has_name(self):
        self.assertEqual("Simona", self.guest.name)
    
    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest.wallet)
    
    def test_can_add_favourite_song(self):
        song1 = Song("mbop", "Hanson")
        self.guest.add_fave_song(song1)
        self.assertEqual(1, len(self.guest.fave_song))
        
    def test_guest_has_favourite_song(self):
        song1 = Song("mbop", "Hanson")
        self.guest.add_fave_song(song1)
        self.assertEqual("mbop", self.guest.fave_song[0].title)
        
    def test_guest_can_cheer_loudly(self):
        self.assertEqual("OH YA DANCER", self.guest.cheer_loudly())
    
    # def test_remove_money_from_wallet(self):
    
    def test_guest_can_pay_entry(self):
        self.guest.pay_entry(self.room)
        self.assertEqual(47.00, self.guest.wallet)


        