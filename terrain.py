
class Ground:
    
    def __init__(self, xpos, ypos, width):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        
    def draw(self, pg, window):
        pg.draw.line(window, (0,255,255), (self.xpos, self.ypos), (self.xpos + self.width, self.ypos),1)
        
        
    def get_x(self):
        return self.xpos
    
    def get_y(self):
        return self.ypos
        
    def get_width(self):
        return self.width