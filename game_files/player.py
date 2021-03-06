import physics
import pygame
import math

class Player:

    """ This class describes how the player will work and interact"""

    def __init__(self, xpos, ypos, direc):

        self._xpos = xpos
        self._ypos = ypos
        self._direc = direc
        
        self._velocity_x = 0
        self._velocity_y = - 20
        self._delta_y = 0
        
        self._grounded = False

        self._movable = ""
        
        self._portal_gun = pygame.image.load("portalgun.png")
        self._portal_gun = pygame.transform.smoothscale(self._portal_gun, (60,30))
        self._portal_rect = self._portal_gun.get_rect()
        self._angle = 180
        
        
    def draw(self, pg, window):
        """ draws the player""" 
        
        # get the new center position that the gun will have to enable better rotation
        x = 30*math.cos(math.radians(self._angle))
        y = 30*math.sin(math.radians(self._angle))

        # get all the correct values for the portalguns draw position
        rot_img = pg.transform.rotate(self._portal_gun, self._angle)
        rot_img_rect = rot_img.get_rect()
        rot_img_rect.center = (self._xpos + 15 + x, self._ypos + 15 - y) # add 15 to x and y to draw out in the center of the player
                                                                         # add x and remove y to draw the gun on a position that will
                                                                         # make it look like it rotates around the players center
        
        # draw it out
        window.blit(rot_img, rot_img_rect)
        
        # draw player
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
            
            # move the player in on the x-axis if there
            # is a velocity
            self._xpos += self._velocity_x
        else:
            # set both x and y velocity to 0 if the player is grounded
            self._velocity_y = 0
            self._velocity_x = 0
            
        self._portal_rect[0], self._portal_rect[1] = self._xpos, self._ypos
        
        
    def move_horizontal(self, direc, dt):
        """ this method moves the player on the x axis
            depending on the direction. 
            It also takes into acount if the player is in the
            air or not, if he is => move slower
                        if not => move faster"""
                        
        if(self._movable == "left" and direc == -1 or
            self._movable == "right" and direc == 1) :
            pass
        else:
            if self._grounded:
                self._xpos += direc * (0.85 + dt) 
            else:
                self._xpos += direc * (0.55 + dt)
                
    def jump(self):
        """ this method makes the player jump if the player is touching the ground"""
        if self._grounded:
            self._velocity_y = -75 # change velocity so the player moves upwards
            self._ypos -= 5 # change the y-pos a little bit so it wont get stuck on the line
    
    
    
    def throw(self, v, angle, dt, terrain_type):
        """ this method takes the velocity, the angle and the
            delta_time as parameters. Then it calls the physics.throw method
            whit these values as arguments so it can calculate the 
            velocity on the x and y axis"""
        
        # if the exiting portal is a ground or roof portal add the speed 
        if(terrain_type == "roof"):
            throw_calc = physics.throw(v, angle,dt)
            self._velocity_x += throw_calc[0]
            self._velocity_y += throw_calc[1]
        
        elif(terrain_type == "ground"):
            throw_calc = physics.throw(v, angle,dt)
            self._velocity_x = throw_calc[0]
            
            # if the terrain_type is ground the player should move upwards 
            # so invert the y speed
            self._velocity_y = self._velocity_y * -0.95 # multiply by -0.95 to prevent the player
                                                        # from increasing in velocity when falling 
                                                        # through the same ground portals
                    
        # if the exiting portal is a wall replace the speed
        elif(terrain_type == "wall"):
            throw_calc = physics.throw(v, angle,dt)
            self._velocity_x = throw_calc[0]
            self._velocity_y = throw_calc[1]
    
    def movable_horizontal(self, state):
        self._movable = state
    
    def get_x(self):
        return self._xpos

    def get_y(self):
        return self._ypos

    def get_direc(self):
        return self._direc
    
    def get_velocity_x(self):
        return self._velocity_x

    
    def get_velocity_y(self):
        return self._velocity_y

    def set_x(self, xpos):
        self._xpos = xpos

    def set_y(self, ypos):
        self._ypos = ypos

    def set_direc(self, direc):
        self._direc = direc
        
    def set_grounded(self, state):
        self._grounded = state
    
    def set_velocity_x(self, v):
        self._velocity_x = v
    
    def set_velocity_y(self, v):
        self._velocity_y = v
        
    def set_angle(self, angle):
        self._angle = math.degrees(-1*angle)
        
