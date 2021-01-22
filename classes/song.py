class Song:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist

    def give_song(self):
        return self.name + " by " + self.artist
