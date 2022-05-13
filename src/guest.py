

class Guest:
    def __init__(self, name, wallet,):
        self.name = name
        self.wallet = wallet
        self.fave_song = []
        
    def add_fave_song(self, song):
        self.fave_song.append(song)

    
    def cheer_loudly(self):
        return "OH YA DANCER"
    
    def pay_entry(self, amount):
        self.wallet -= amount.entry_fee
    
        
        