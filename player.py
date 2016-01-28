import physics


class Player:

    """ This class describes how the player will work and interact"""

    def __init__(self, xpos, ypos, direc):

        self._xpos = xpos
        self._ypos = ypos
        self._direc = direc
        
        self._velocity_y = - 20
        self._delta_y = 0
        
        self._grounded = False

    def draw(self, pg, window):
        """ draws the player""" 
        rect = pg.Rect(self._xpos, self._ypos, 30,50)
        color = (0,0,0)
        
        pg.draw.rect(window,color,rect,5)
    
    def update(self, dt):
        """ update method"""
        
        if not self._grounded:
            # call the gravity function to move the player in a 
            # kinda realistic way
            gravity_calc = physics.gravity(self._velocity_y, dt)
            self._ypos += gravity_calc[0]
            self._velocity_y = gravity_calc[1]
        else:
            self._velocity_y = 0
        
    def move_horizontal(self, direc, dt):
        """ this method moves the player on the x axis
            depending on the direction. 
            It also takes into acount if the player is in the
            air or not, if he is => move slower
                        if not => move faster"""
        if self._grounded:
            self._xpos += direc * (0.75 + dt)
        else:
            self._xpos += direc * (0.15 + dt)
            
    def jump(self):
        """ this method makes the player jump if the player is touching the ground"""
        if self._grounded:
            self._velocity_y = -50 # change velocity so the player moves upwards
            self._ypos -= 5 # change the y-pos a little bit so it wont get stuck on the line
    
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
        
    def set_grounded(self, state):
        self._grounded = state
