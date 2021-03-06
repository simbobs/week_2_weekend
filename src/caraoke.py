
class Caraoke:
    def __init__(self, name):
        self.name = name
        self._rooms = []
        self._till_total = 0.00
    
    def add_room(self, room):
        self._rooms.append(room)
    
    def collect_entry_fee(self, room):
        self._till_total += room.entry_fee
        
    def check_in_guest(self, guest, room):
        if room.count_guests() == room.capacity:
            return
        else:
            room.add_guest(guest)
            guest.pay_entry(room)
            self.collect_entry_fee(room)
    
    def find_room(self, room):
        for suite in self._rooms:
            if suite == room:
                return suite
            
    
    def check_out_guest(self, guest, room):
        self.find_room(room).remove_guest(guest)
        
        
        
        