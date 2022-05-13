import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Complicated", "Avril Lavigne")
    
    def test_song_has_title(self):
        self.assertEqual("Complicated", self.song.title)
    
    def test_song_has_artist(self):
        self.assertEqual("Avril Lavigne", self.song.artist)
    
    
        
        