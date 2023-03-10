# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
from _operator import contains


class Black_Hole(Simulton):  
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        
    def update(self, model):
        preys = model.find(lambda x: isinstance(x, Prey) and Black_Hole.contains(self, x.get_location()))
        for i in preys:
            model.remove(i)
        return preys
        
    def display(self, canvas):
        canvas.create_oval(self.get_location()[0] - (self.get_dimension()[0]/2), self.get_location()[1] - (self.get_dimension()[1]/2), self.get_location()[0] + (self.get_dimension()[0]/2), self.get_location()[1] + (self.get_dimension()[1]/2), fill='black')
        
    def contains(self,xy):
        dem = self.get_location()
        if Black_Hole.radius > abs(dem[0] - xy[0]) and Black_Hole.radius > abs(dem[1] - xy[1]):
            return True