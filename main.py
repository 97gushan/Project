import pygame

pygame.init()


def update(delta_time):
    """ this method handels all the things that will happen
        every time the code runs"""
    pass
    
def draw():
    """ this method handels the draws on the screen"""
    pass

def input():
    """ this method checks for input from the user"""
    for event in pygame.event.get():
        
        # check for quit event
        if(event.type == pygame.QUIT):
            global is_running
            is_running = False


# Setting up the window
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Portal")

clock = pygame.time.Clock()



is_running = True

# create the game loop
while is_running:
    delta_time = clock.tick() / 1000
    print(delta_time)
    
    
    input()
    update(delta_time)
    draw()
    
    pygame.display.update()
