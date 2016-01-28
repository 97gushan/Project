
class Player:
    """ This class describes how the player will work and interact"""

    def __init__(self, xpos, ypos, direc):

        self._xpos = xpos
        self._ypos = ypos
        self._direc = direc
        
        self._delta_t = 0.025
        self._velocity_y = - 50
        self._delta_y = 0

    def draw(self, pg, window):
        """ draws the player""" 
        rect = pg.Rect(self._xpos, self._ypos, 30,50)
        color = (0,0,0)
        
        pg.draw.rect(window,color,rect,5)
    
    def update(self, dt):
        """ update method"""
        self._velocity_y = self._velocity_y + (self._delta_t + dt) * 9.82
        self._delta_y = (self._delta_t + dt) * self._velocity_y
        self._ypos += self._delta_y
        
    
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
