# 1. initialize pygame
import pygame
pygame.init()

# 2. colors variables
black = ( 0, 0, 0 )
white = ( 255, 255, 255 )

# 3. screen size
screen_size = ( 800,600 )

# 4. create the windows
screen = pygame.display.set_mode( screen_size )
 
clock = pygame.time.Clock()

game_over = False
# 5. game loop
# that is another way to define the game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # 6. fill the screen with color
    screen.fill( black )

    # 7. refresh the windows
    pygame.display.flip()
    
pygame.quit()