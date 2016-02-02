import pygame
from math import atan2
import player
import terrain
import portal
import portal_positioner

class Game:
    def __init__(self):
        # Setting up the window
        self.window = pygame.display.set_mode((900,800))
        pygame.display.set_caption("Portal")

        self.clock = pygame.time.Clock()
        
        self.is_running = True
        
        self.delta_time = 0
        
        self.player = player.Player(70,100,2)
        
        self.ground = [terrain.Ground(0,300,300),terrain.Ground(300,600,400),
                       terrain.Ground(700,400,200)]
        
        self.wall = [terrain.Wall(300,300,300,"left"),terrain.Wall(700,400,200,"right"),
                     terrain.Wall(0,0,300,"left"),terrain.Wall(899,0,400,"right"),]
                     
        self.roof = [terrain.Roof(0,0,900)]
                     
        self.portal_1 = portal.Portal(0,0,(255,0,0),0)
        self.portal_2 = portal.Portal(0,0,(0,0,255),0)
        
        self.portal_positioner = portal_positioner.Portal_Positioner()
        
    def update(self):
        """ this method handels all the things that will happen
            every time the code runs"""
            
        # create the game loop
        while self.is_running:
        
            # get the delta time and set frame lock to 400 frames
                # I did not want a framelock but the game was not smooth
                # when no number was added so i chose a high cap of framerate
            self.delta_time = self.clock.tick(400) / 1000
                
            self.check_collision()
            
            
            self.player.update(self.delta_time)
            
            self.portal_positioner.move(self.delta_time)
            
            self.input()
            self.draw()
            
            pygame.display.update()
        
    def draw(self):
        """ this method handels the draws on the screen"""
        self.window.fill((255,255,255))
        
        self.player.draw(pygame, self.window)
        
        # draw all the ground
        for n in range(len(self.ground)):
            self.ground[n].draw(pygame, self.window)
            
        # draw all the walls    
        for n in range(len(self.wall)):
            self.wall[n].draw(pygame, self.window)
        
        # draw all of the roofs
        for n in range(len(self.roof)):
            self.roof[n].draw(pygame, self.window)
        
        # draws the two portals
        self.portal_1.draw(pygame, self.window)
        self.portal_2.draw(pygame, self.window)
        
        # draws the positioner
        self.portal_positioner.draw(pygame, self.window)
    
    def place_portal(self, type, terrain_size):
        """ this method places the portal on the place that the positioner landed.
            which portal that is placed depends on the portal_positioners _portal value."""
        
        if(self.portal_positioner.get_portal() == "left"):
            self.portal_1.set_terrain_type(type)
            
            # check if the portal will be placed beneath the wall, 
            # if it is going to move it upp so the bottom of the portal 
            # ends at the same position as the bottom of the wall
            if(type == "wall" and self.portal_positioner.get_y() + 70 > terrain_size):
                self.portal_1.set_y(terrain_size-70)
                self.portal_1.set_x(self.portal_positioner.get_x())
                
            # check if the portal will be placed to far to the right,
            # if it is move it left so the right end of the portal
            # is placed where the ground ends to the right
            elif(type == "ground" and self.portal_positioner.get_x() + 70 > terrain_size):
                self.portal_1.set_x(terrain_size-70)
                self.portal_1.set_y(self.portal_positioner.get_y())
            
            # the position is clear to place on
            else:
                self.portal_1.set_y(self.portal_positioner.get_y())
                self.portal_1.set_x(self.portal_positioner.get_x())


            self.portal_1.set_active(True)
            
        elif(self.portal_positioner.get_portal() == "right"):
            self.portal_2.set_terrain_type(type)
            
            # as above but for portal_2
            if(type == "wall" and self.portal_positioner.get_y() + 70 > terrain_size):
                self.portal_2.set_y(terrain_size-70)
                self.portal_2.set_x(self.portal_positioner.get_x())
            # as above but for portal_2
            elif(type == "ground" and self.portal_positioner.get_x() + 70 > terrain_size):
                self.portal_2.set_x(terrain_size-70)
                self.portal_2.set_y(self.portal_positioner.get_y())
            else:
                self.portal_2.set_y(self.portal_positioner.get_y())
                self.portal_2.set_x(self.portal_positioner.get_x())
            
            self.portal_2.set_active(True)
        
        # disables the positioenr
        self.portal_positioner.set_active(False)
    
    def check_collision(self):
        """ this method controlls the collision detection of everything 
            in this game"""

        player_x = self.player.get_x()
        player_y = self.player.get_y() + 50 # player position plus the height to check collision under it
        
        positioner_x = self.portal_positioner.get_x()
        positioner_y = self.portal_positioner.get_y()
        
        # player and ground collision
        for n in range(len(self.ground)):
            ground_x = self.ground[n].get_x()
            ground_y = self.ground[n].get_y()
            ground_w = self.ground[n].get_width() + self.ground[n].get_x()
            
            # check if the player touches the ground
            if(player_y > ground_y-5 and player_x + 30 > ground_x and player_x < ground_w):
                self.player.set_grounded(True)
                break
            else:
                self.player.set_grounded(False)     # did not touch so set grounded to false
        
        

    
        # player and wall collision
        for n in range(len(self.wall)):
            wall_x = self.wall[n].get_x()
            wall_y = self.wall[n].get_y()
            wall_h = self.wall[n].get_height() + self.wall[n].get_y()
            wall_d = self.wall[n].get_direc()
            
            # check if the player touches the left wall
            if(wall_d == "left"):
                if(player_x < wall_x + 5 and player_y > wall_y + 5 and player_y < wall_h):
                    self.player.movable_horizontal("left")
                    break
                else: 
                    self.player.movable_horizontal("")

            # check if the player touches the left wall                    
            elif(wall_d == "right"):
                if(player_x + 30 > wall_x - 5 and player_y > wall_y and player_y < wall_h):
                    self.player.movable_horizontal("right")
                    break
                else: 
                    self.player.movable_horizontal("")
        
        
        """ check for collision between the portal positioner and the terrain"""
        if(self.portal_positioner.get_active()):
        
            # ground
            for n in range(len(self.ground)):
                ground_x = self.ground[n].get_x()
                ground_y = self.ground[n].get_y()
                ground_w = self.ground[n].get_width() + self.ground[n].get_x()
                
                
                # check if the positioner touches the ground
                if(positioner_y > ground_y-5 and positioner_x > ground_x and positioner_x < ground_w):
                    self.place_portal("ground", ground_w)
                    break
                        
            # wall
            for n in range(len(self.wall)):
                wall_x = self.wall[n].get_x()
                wall_y = self.wall[n].get_y()
                wall_h = self.wall[n].get_height() + self.wall[n].get_y()
                wall_d = self.wall[n].get_direc()
                
                # check if the positioner touches the left wall
                if(wall_d == "left"):
                    if(positioner_x < wall_x + 5 and positioner_y > wall_y + 5 and positioner_y < wall_h):
                        self.place_portal("wall", wall_h)
                        break

                        
                # check if the positioner touches the right wall
                elif(wall_d == "right"):
                    if(positioner_x +5 > wall_x - 5 and positioner_y > wall_y and positioner_y < wall_h):
                        self.place_portal("wall", wall_h)
                        break
        
    def input(self):
        """ this method checks for input from the user"""
        
        # mouse position
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        
        for event in pygame.event.get():
            
            # check for quit event
            if(event.type == pygame.QUIT):
                self.is_running = False
                
        # check for keyboard input        
        pressed = pygame.key.get_pressed()
        
        if(pressed[pygame.K_d]):
            self.player.move_horizontal(1,self.delta_time)
        if(pressed[pygame.K_a]):
            self.player.move_horizontal(-1,self.delta_time)

        if(pressed[pygame.K_SPACE]):
            self.player.jump()
        
        # removes both portal 
        if(pressed[pygame.K_r]):
            self.portal_1.set_active(False)
            self.portal_2.set_active(False)
        
        # check for mouse input
        pressed = pygame.mouse.get_pressed()
        
        # check if left mouse button is pressed
        if(pressed[0]):
           
            # get the x and y values between the player and the mouse
            x = mouse_x - self.player.get_x()
            y = mouse_y - self.player.get_y()
            
            # calculate the angle
            angle = atan2(y,x)
            
            # call all the necesary methods of the portal_positioner object
            self.portal_positioner.set_x(self.player.get_x()) # position
            self.portal_positioner.set_y(self.player.get_y())
            self.portal_positioner.set_active(True)           # make it active
            self.portal_positioner.set_portal("left")         # type of portal that it will place
            self.portal_positioner.set_angle(angle)           # which angle it will fly away with
            print("left is pressed")
        
        # check if right mouse button is pressed
        if(pressed[2]):
            # get the x and y values between the player and the mouse
            x = mouse_x - self.player.get_x()
            y = mouse_y - self.player.get_y()
            
            # calculate the angle
            angle = atan2(y,x)
            
            # call all the necesary methods of the portal_positioner object
            # se above for explanation
            self.portal_positioner.set_x(self.player.get_x())
            self.portal_positioner.set_y(self.player.get_y())
            self.portal_positioner.set_active(True)
            self.portal_positioner.set_portal("right")
            self.portal_positioner.set_angle(angle)

def run():

    pygame.init()
    
    game = Game()
    game.update()
    

if(__name__ == "__main__"):
    run()
