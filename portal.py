class Portal:
    """ this class describes how the portals will work"""
    def __init__(self, xpos, ypos, color, angle):
        self._xpos = xpos
        self._ypos = ypos
        self._color = color
        self._angle = angle
    
        self._active = False
    
    def draw(self, pg, window):
        """ draw the portal"""
        if(self._active):
            rect = pg.Rect(self._xpos, self._ypos, 30,50)
            
            pg.draw.rect(window,self._color,rect,0)
    
    
    # get  and set methods
    def get_x(self):
        return self._xpos

    def get_y(self):
        return self._ypos

    def get_angle(self):
        return self._angle
        
    def get_active(self):
        return self._active

    def set_x(self, xpos):
        self._xpos = xpos

    def set_y(self, ypos):
        self._ypos = ypos
    
    def set_angle(self, angle):
        self._angle = angle
        
    def set_active(self, state):
        self._active = state