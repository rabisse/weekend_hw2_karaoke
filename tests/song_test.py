import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("What Is Love", "Haddaway")

    def test_song_name(self):
        self.assertEqual("What Is Love", self.song.name)
    
    def test_song_artist(self):
        self.assertEqual("Haddaway", self.song.artist)

    def test_give_song(self):
        self.assertEqual("What Is Love by Haddaway", self.song.give_song())
