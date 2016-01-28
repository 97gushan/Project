
class Player:
    """ This class describes how the player will work and interact"""

    def __init__(self, xpos, ypos, direc):

        self.xpos = xpos
        self.ypos = ypos
        self.direc = direc

    def get_x(self):
        return self.xpos

    def get_y(self):
        return self.ypos

    def get_direc(self):
        return self.direc

    def set_x(self, xpos):
        self.xpos = xpos

    def set_y(self, ypos):
        self.ypos = ypos

    def set_direc(self, direc):
        self.direc = direc
