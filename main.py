import pygame

import player

class Game:
    def __init__(self):
        # Setting up the window
        self.window = pygame.display.set_mode((500,500))
        pygame.display.set_caption("Portal")

        self.clock = pygame.time.Clock()
        
        self.is_running = True
        
        self.delta_time = 0
        
        self.player = player.Player(70,100,2)
        
    def update(self):
        """ this method handels all the things that will happen
            every time the code runs"""
            
        # create the game loop
        while self.is_running:
            self.delta_time = self.clock.tick(400) / 1000
            #print(delta_time)
            
            
            self.input()
            
            self.player.update(self.delta_time)
            
            self.draw()
            
            pygame.display.update()
        
    def draw(self):
        """ this method handels the draws on the screen"""
        self.window.fill((255,255,255))
        
        self.player.draw(pygame, self.window)

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
