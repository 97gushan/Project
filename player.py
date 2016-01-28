
class Player:
    """ This class describes how the player will work and interact"""

    def __init__(self, xpos, ypos, direc):

        self._xpos = xpos
        self._ypos = ypos
        self._direc = direc
        


    def draw(self, pg, window):
        """ draws the player""" 
        rect = pg.Rect(self._xpos, self._ypos, 30,50)
        color = (0,0,0)
        
        pg.draw.rect(window,color,rect,5)
    

        
    
    def get_x(self):
        return self._xpos

    def get_y(self):
        return self._ypos

    def get_direc(self):
        return self._direc

    def set_x(self, xpos):
        self._xpos = xpos

    def set_y(self, ypos):
        self._ypos = ypos

    def set_direc(self, direc):
        self._direc = direc
