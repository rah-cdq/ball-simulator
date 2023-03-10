# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,2, 5)
        self.randomize_angle()
        # self.ufo_img = PhotoImage(file='ufo.gif')
        
    def update(self, model):
        if random() <= 0.3:
            self._speed = self._speed + (random() - 0.5)
            if self._speed < 3: self._speed = 3
            if self._speed > 7: self._speed = 7
            self._angle = self._angle + (random() - 0.5)
        self.move()
        self.wall_bounce()
        
    def display(self, canvas):
        canvas.create_oval(self._x - Floater.radius, self._y - Floater.radius, self._x + Floater.radius, self._y + Floater.radius, fill='red')

