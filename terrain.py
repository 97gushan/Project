class Terrain:
    def __init__(self, xpos, ypos):
        self._xpos = xpos
        self._ypos = ypos
    
    # get methods
    def get_x(self):
        return self._xpos
    
    def get_y(self):
        return self._ypos


class Ground (Terrain):
    """ this class describes how the ground will work"""
    def __init__(self, xpos, ypos, width):
        
        super().__init__(xpos, ypos)

        self._width = width
        
    def draw(self, pg, window):
        
        box_color = (45,45,45)
        line_color = (0,255,255)
        
        # draw out ground beneath the line
        height = 800 - self._ypos
        rect = pg.Rect(self._xpos, self._ypos, self._width,height)
        
        pg.draw.rect(window,box_color,rect,0)
        pg.draw.line(window, line_color, (self._xpos, self._ypos), (self._xpos + self._width, self._ypos),1)
        
    # get methods   
    def get_width(self):
        return self._width
        

class Wall(Terrain):
    """ this class describes how the walls will work"""
    
    def __init__(self, xpos, ypos, height, direc):
        super().__init__(xpos, ypos)
        self._height = height
        self._direc = direc
        
    def draw(self, pg, window):
        pg.draw.line(window, (0,255,255), (self._xpos, self._ypos), (self._xpos, self._ypos + self._height),1)
        
    
    # get methods    
    def get_height(self):
        return self._height
        
    def get_direc(self):
        return self._direc