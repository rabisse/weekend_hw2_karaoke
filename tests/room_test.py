import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("What Is Love", "Haddaway")
        self.song_2 = Song("Stayin Alive", "The Bee Gees")
        self.room = Room("Roxbury", 2, 20)
        self.guest_1 = Guest("Steve Butabi", 100, "What Is Love")
        self.guest_2 = Guest("Doug Butabi", 80, "Stayin Alive")
        self.guest_3 = Guest("Malcolm Holwill", 10, "What Is Love")
        self.guest_4 = Guest("Katie Jeffree",50, "Stayin Alive")

    def test_room_name(self):
        self.assertEqual("Roxbury", self.room.name)

    def test_room_capacity(self):
        self.assertEqual(2, self.room.capacity)

    def test_room_entry_fee(self):
        self.assertEqual(20, self.room.entry_fee)
    
    def test_add_song_to_song_queue(self):
        self.room.add_song_to_song_queue(self.song_1)
        self.assertEqual(1, len(self.room.song_queue))

    def test_favorite_song_response(self):
        self.room.add_guest_to_room(self.guest_1)
        self.assertEqual(["Steve Butabi loves the song What Is Love!"], self.room.add_song_to_song_queue(self.song_1))

    def test_not_favorite_song_add(self):
        self.room.add_guest_to_room(self.guest_2)
        self.assertEqual([], self.room.add_song_to_song_queue(self.song_1))

    def test_print_song_queue(self):
        self.room.add_song_to_song_queue(self.song_1)
        self.room.add_song_to_song_queue(self.song_2)
        self.assertEqual(['What Is Love by Haddaway', 'Stayin Alive by The Bee Gees'], self.room.give_song_queue())

    def test_room_bill(self):
        self.assertEqual(0, self.room.bill)

    def test_starting_occupancy(self):
        self.assertEqual(0, self.room.num_of_occupants())

    # check that money left guest, money added to room bill, and guest obj in room occupants list
    def test_add_guest_to_room_success(self):
        self.room.add_guest_to_room(self.guest_1)
        self.assertEqual(1, self.room.num_of_occupants())
        self.assertEqual(20, self.room.total_room_bill())
        self.assertEqual(80, self.guest_1.wallet)

    def test_add_two_guests(self):
        self.room.add_guest_to_room(self.guest_1)
        self.room.add_guest_to_room(self.guest_2)
        self.assertEqual(2, self.room.num_of_occupants())
        self.assertEqual(40, self.room.total_room_bill())

    def test_add_guest_to_room_full(self):
        self.room.add_guest_to_room(self.guest_1)
        self.room.add_guest_to_room(self.guest_2)
        self.room.add_guest_to_room(self.guest_4)
        self.assertEqual(2, self.room.num_of_occupants())
    # is it better to assert the list length or return a string? I would think printing the string makes more sense for real situations, or testing both?

    def test_add_guest_to_room_not_enough_money(self):
        self.room.add_guest_to_room(self.guest_3)
        self.assertEqual(0, self.room.num_of_occupants())

    def test_clear_out_room(self):
        self.room.add_guest_to_room(self.guest_1)
        self.room.add_guest_to_room(self.guest_2)
        self.room.clear_out_room()
        self.assertEqual(0, self.room.bill)
        self.assertEqual(0, self.room.num_of_occupants())
