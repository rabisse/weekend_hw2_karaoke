class Room:
    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.song_queue = []
        self.bill = 0
        self.occupants = []

    def num_of_occupants(self):
        return len(self.occupants)

    def add_song_to_song_queue(self, song):
        self.song_queue.append(song)
        fav_song = [f"{guest.name} loves the song {song.name}!" for guest in self.occupants if guest.favorite_song == song.name]
        print(fav_song)
        return fav_song    # how can I simplify this?

    def give_song_queue(self):
        return [song.give_song() for song in self.song_queue]

    def total_room_bill(self):
        return self.bill

    def add_guest_to_room(self, guest):
        if self.num_of_occupants() < self.capacity:
            if guest.wallet >= self.entry_fee:
                guest.wallet -= self.entry_fee
                self.bill += self.entry_fee
                self.occupants.append(guest)
                
                print("Guest added")
            else: print("Guest needs some money if they wanna sing!")
        else: print("This room is full!")

    def clear_out_room(self):
        self.bill = 0
        self.occupants = []  #does this do the same thing as self.occupants.clear() ?
        print("Room is clear")
