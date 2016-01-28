import pygame

import player
import terrain

class Game:
    def __init__(self):
        # Setting up the window
        self.window = pygame.display.set_mode((500,500))
        pygame.display.set_caption("Portal")

        self.clock = pygame.time.Clock()
        
        self.is_running = True
        
        self.delta_time = 0
        
        self.player = player.Player(70,100,2)
        
        self.ground = terrain.Ground(0,400,300)
        
    def update(self):
        """ this method handels all the things that will happen
            every time the code runs"""
            
        # create the game loop
        while self.is_running:
            self.delta_time = self.clock.tick(400) / 1000
            #print(delta_time)
            
            self.check_collision()
            
            self.input()
            
            self.player.update(self.delta_time)
            
            self.draw()
            
            pygame.display.update()
        
    def draw(self):
        """ this method handels the draws on the screen"""
        self.window.fill((255,255,255))
        
        self.player.draw(pygame, self.window)
        
        self.ground.draw(pygame, self.window)
    
    def check_collision(self):
        """ this method controlls the collision detection of everything 
            in this game"""

        player_x = self.player.get_x()
        player_y = self.player.get_y() + 50 # player position plus the height to check collision under it
            
        # player and ground collision
        ground_x = self.ground.get_x()
        ground_y = self.ground.get_y()
        ground_w = self.ground.get_width() + self.ground.get_x()
        
        if(player_y > ground_y and player_x >= ground_x and player_x < ground_w):
            self.player.set_grounded(True)
        else:
            self.player.set_grounded(False)
    
    
    def input(self):
        """ this method checks for input from the user"""
        
        # mouse position
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        #print(mouse_x, mouse_y)
        
        for event in pygame.event.get():
            
            # check for quit event
            if(event.type == pygame.QUIT):
                self.is_running = False




def run():

    pygame.init()
    
    game = Game()
    game.update()
    

if(__name__ == "__main__"):
    run()
