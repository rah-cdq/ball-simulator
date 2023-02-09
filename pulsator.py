# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    counter = 30
    
    def __init__(self,x,y):
        Black_Hole.__init__(self, x, y)
        self.tbm = 0
        
    def update(self, model):
        self.tbm += 1
        f = Black_Hole.update(self, model)
        
        if len(f) >= 1:
            self.change_dimension(len(f),len(f))
            self.tbm = 0
        
        if self.tbm >= Pulsator.counter:
            self.change_dimension(-1, -1)
            
            
        if self.get_dimension() <= (0,0):
            model.remove(self)