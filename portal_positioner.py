from math import cos, sin

class Portal_Positioner:
    def __init__(self):
        self._xpos = 100
        self._ypos = 100
        self._angle = 0
        self._active = False
        self._portal = ""
        
    def draw(self, pg, window):
        """ draw the portal"""
        if(self._active):
            rect = pg.Rect(self._xpos, self._ypos, 5,5)
            
            pg.draw.rect(window,(0,255,0),rect,0)
    
    def move(self, dt):
        """ this method moves the positioner in the correct direction
            acording to the angle that is set"""
        if(self._active):
            self._xpos += 1000 * dt * cos(self._angle)
            self._ypos += 1000 * dt * sin(self._angle)
            
    def get_x(self):
        return self._xpos

    def get_y(self):
        return self._ypos

    def get_angle(self):
        return self._angle
        
    def get_active(self):
        return self._active
    
    def get_portal(self):
        return self._portal

    def set_x(self, xpos):
        self._xpos = xpos

    def set_y(self, ypos):
        self._ypos = ypos
    
    def set_angle(self, angle):
        self._angle = angle
        
    def set_active(self, state):
        self._active = state
        
    def set_portal(self, state):
        self._portal = state
        
        
        
        
