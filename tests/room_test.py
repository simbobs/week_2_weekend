import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Sashay", 5, 3.00)
        self.room2 = Room("Cher", 3, 5)
        self.guest1 = Guest("Simona", 50)
        self.guest2 = Guest("Lorena", 100)
        self.song1 = Song("mbop", "Hanson")
        self.song2 = Song("complicated", "Avril Lavigne")
    
    def test_room_has_number(self):
        self.assertEqual("Sashay", self.room.name)
    
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity)
    
    def test_room_has_entry_fee(self):
        self.assertEqual(3.00, self.room.entry_fee)
        
    def test_can_add_guest_to_room(self):
        self.room.add_guest(self.guest1)
        self.room.add_guest(self.guest2)
        self.assertEqual(2, len(self.room._guests))
    
    def test_can_remove_guest_from_room(self):
        self.room.add_guest(self.guest1)
        self.room.add_guest(self.guest2)
        self.room.remove_guest(self.guest1)
        self.assertEqual(1, len(self.room._guests))
        self.assertEqual ("Lorena", self.room._guests[0].name)
    
    
    
    ## you've added methods to remove/add guests - so next step to
    # check in guest, need a test to call those methods (if statement for capacity?)
    # and call guest method to pay entry
    
    def test_room_can_add_song_to_list(self):
        self.room.add_song(self.song1)
        self.room.add_song(self.song2)
        self.assertEqual(2, len(self.room._songs))
    
    def test_can_add_money_to_till(self):
        self.room.add_money_to_till(4)
        self.assertEqual(4, self.room._till)
        
    
    def test_check_how_many_people_are_in_the_room(self):
        self.room.add_guest(self.guest1)
        self.room.add_guest(self.guest2)
        self.room.count_guests()
        self.assertEqual(2, len(self.room._guests))
        
    # def test_room_can_play_song(self):
    #     self.room.add_song(self.song1)
    #     self.room.add_song(self.song2)
    #     self.room.add_guest(self.guest1)
    #     self.guest1.add_fave_song(self.song1)
    #     self.room.play_song(self.room._songs, self.room._guests)
    #     self.assertEqual("OH YA DANCER", self.room.play_song())
  
    
    