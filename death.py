from datetime import datetime

class death:
    
    # init method or constructor 
    def __init__(self, count, reason, location):
        self.death_count = count
        self.death_reason = reason
        self.death_location = location
        self.death_time = datetime.now().strftime("%c")
        
    def update(self, count, reason, location):
        self.death_count = count
        self.death_reason = reason
        self.death_location = location
        self.death_time = datetime.now().strftime("%c")
        
    def to_string(self):
        return "Death %d: Killed by %s in %s on %s"%(self.death_count, self.death_reason, self.death_location, self.death_time)