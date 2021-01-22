import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Steve Butabi", 100, "What Is Love")
    
    def test_guest_name(self):
        self.assertEqual("Steve Butabi", self.guest.name)

    def test_guest_wallet(self):
        self.assertEqual(100, self.guest.wallet)

    def test_guest_favorite_song(self):
        self.assertEqual("What Is Love", self.guest.favorite_song)
