# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
import math
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    
    distance = 200
    
    def __init__(self,x,y):
        Mobile_Simulton.__init__(self, x, y, 20, 20, 0, 5)
        Pulsator.__init__(self, x, y)

        self.randomize_angle()
        self.target = None

    def update(self, model):
        Pulsator.update(self, model)
        preyers = model.find(lambda x: isinstance(x, Prey))
        if len(preyers) != 0:
            #print(preyers)
            preyers2 = list(preyers)
            preyers2 = sorted(preyers2, key=lambda x: math.sqrt(((x.get_x()-self.get_x()) * (x.get_x()-self.get_x())) + ((x.get_y() - self.get_y()) * (x.get_y() - self.get_y()))))
            if self.target is None:
                self.target = preyers2[0]

            else:

                if (math.sqrt(((self.target.get_x() - self.get_x()) *
                               (self.target.get_x() - self.get_x())) +
                              ((self.target.get_y() - self.get_y()) *
                               (self.target.get_y() - self.get_y())))) > 200:
                    self.target = preyers2[0]

                if self.target in preyers2:
                    if (self.target.get_x() < self.get_x()):
                        angle = -1 * ( (self.target.get_x()-self.get_x())/(self.target.get_y() - self.get_y()) )
                    else:
                        angle = (self.target.get_y() - self.get_y()) / (self.target.get_x() - self.get_x())
                    self.set_angle(angle)
                else:
                    self.target = preyers2[0]
                    if (self.target.get_x() < self.get_x()):
                        angle = -1 * ( (self.target.get_x()-self.get_x())/(self.target.get_y() - self.get_y()) )
                    else:
                        angle = (self.target.get_y() - self.get_y()) / (self.target.get_x() - self.get_x())

                    #print(angle)
                    self.set_angle(angle)

        #self.set_angle(preyers)
        self.move()
