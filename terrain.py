
class Ground:
    """ this class describes how the ground will work"""
    def __init__(self, xpos, ypos, width):
        self._xpos = xpos
        self._ypos = ypos
        self._width = width
        
    def draw(self, pg, window):
        pg.draw.line(window, (0,255,255), (self._xpos, self._ypos), (self._xpos + self._width, self._ypos),1)
        
        
    def get_x(self):
        return self._xpos
    
    def get_y(self):
        return self._ypos
        
    def get_width(self):
        return self._width
        

class Wall:
    """ this class describes how the walls will work"""
    
    def __init__(self, xpos, ypos, height, direc):
        self._xpos = xpos
        self._ypos = ypos
        self._height = height
        self._direc = direc
        
    def draw(self, pg, window):
        pg.draw.line(window, (0,255,255), (self._xpos, self._ypos), (self._xpos, self._ypos + self._height),1)
        
        
    def get_x(self):
        return self._xpos
    
    def get_y(self):
        return self._ypos
        
    def get_height(self):
        return self._height
        
    def get_direc(self):
        return self._direc