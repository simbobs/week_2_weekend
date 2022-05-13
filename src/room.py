from src.guest import Guest

class Room:
    
    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self._guests = []
        self._songs = []
        self._till = 0
    
    def add_guest(self, guest):
        self._guests.append(guest)
        
    def remove_guest(self,guest):
        for person in self._guests:
            if guest == person:
                self._guests.remove(guest)
        return self._guests
    
    def add_song(self, song):
        self._songs.append(song)
    
    def add_money_to_till(self, amount):
        self._till += amount
    
    def count_guests(self):
        return len(self._guests)
    
 
        
    
    