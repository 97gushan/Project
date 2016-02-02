class Portal:
    """ this class describes how the portals will work"""
    def __init__(self, xpos, ypos, color, angle):
        self._xpos = xpos
        self._ypos = ypos
        self._color = color
        self._angle = angle
    
        self._active = False
        self._terrain_type = ""

    
    def draw(self, pg, window):
        """ draw the portal"""
        if(self._active):
            if(self._terrain_type == "wall"):

                rect = pg.Rect(self._xpos, self._ypos, 10,70)
            
                pg.draw.rect(window,self._color,rect,0)
                
            elif(self._terrain_type == "ground" or self._terrain_type == "roof"):

                rect = pg.Rect(self._xpos, self._ypos, 70,10)
            
                pg.draw.rect(window,self._color,rect,0)
    
    def get_teleportation_point(self):
        if(self._terrain_type == "ground"):
            return [self._xpos+20, self._ypos-80]
        elif(self._terrain_type == "roof"):
            return [self._xpos+20, self._ypos+10]    
    
    # get  and set methods
    def get_x(self):
        return self._xpos

    def get_y(self):
        return self._ypos

    def get_angle(self):
        return self._angle
        
    def get_active(self):
        return self._active
    
    def get_terrain_type(self):
        return self._terrain_type

    def set_x(self, xpos):
        self._xpos = xpos

    def set_y(self, ypos):
        self._ypos = ypos
    
    def set_angle(self, angle):
        self._angle = angle
        
    def set_active(self, state):
        self._active = state
        
    def set_terrain_type(self, type):
        self._terrain_type = type