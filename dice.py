import random

class Dice():
    """A siple attempt to model dice."""
    def __init__(self, faces):
	    self.faces = faces

    def throw(self):
        d1 = random.randint(0,self.faces)
        print (d1)
        #return d1


dice_1 = Dice(12)
dice_1.throw()
