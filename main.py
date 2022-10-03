# 1. initialize pygame
import pygame
pygame.init()

# 2. colors variables
black = ( 0, 0, 0 )
white = ( 255, 255, 255 )
light_grey = ( 200, 200, 200 )

# 3. screen size
screen_width = 800
screen_height = 600
screen_size = ( screen_width, screen_height )

# 11. define the player constants
player_width = 15
player_height = 90

# 11.1 Coordinates player 1
player_1_x_coord = 50
player_1_y_coord = int( 300 - ( player_height / 2 ) ) # we use int function to save as integer
player_1_y_speed = 0

# 11.1 Coordinates player 2
player_2_y_coord = player_1_y_coord
player_2_x_coord = 750 - player_width
player_2_y_speed = 0

# 11.2 ball coordinates
ball_x_coord = 400
ball_y_coord = 300
ball_radius = 10

ball_speed_x = 5
ball_speed_y = 5

# 4. create the windows
screen = pygame.display.set_mode( screen_size )
pygame.display.set_caption("ADA-pong")

# 5. to refresh the screen
clock = pygame.time.Clock()

game_over = False
# 6. game loop
# that is another way to define the game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        # 13. players movement
        if event.type == pygame.KEYDOWN:
            # 13.1 player 1
            if event.key == pygame.K_w:
                player_1_y_speed = -10

            if event.key == pygame.K_s:
                player_1_y_speed = 10
            
            # 13.2 player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = -10

            if event.key == pygame.K_DOWN:
                player_2_y_speed = 10
        
        # when release the key
        if event.type == pygame.KEYUP:
            # 13.1 player 1
            if event.key == pygame.K_w:
                player_1_y_speed = 0

            if event.key == pygame.K_s:
                player_1_y_speed = 0
            # 13.2 player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = 0

            if event.key == pygame.K_DOWN:
                player_2_y_speed = 0

    # ball boundary: top or bottom
    if ball_y_coord > (screen_height - ball_radius) or ball_y_coord < ball_radius:
        ball_speed_y *= -1

    # ball boundary: right or left
    if (ball_x_coord > screen_width) or (ball_x_coord < 0):
        
        ball_x_coord = int( screen_width / 2 ) # we use int function to save as integer
        ball_y_coord = int( screen_height / 2 )
        ball_speed_x *= -1

    # players and ball movement
    player_1_y_coord += player_1_y_speed
    player_2_y_coord += player_2_y_speed

    # player 1 boundary
    if player_1_y_coord <= 0:
        player_1_y_coord = 0

    if player_1_y_coord >= (screen_height - player_height):
        player_1_y_coord = screen_height - player_height

    # player 2 boundary
    if player_2_y_coord <= 0:
        player_2_y_coord = 0

    if player_2_y_coord >= (screen_height - player_height):
        player_2_y_coord = screen_height - player_height
    
    # ball movement
    ball_x_coord += ball_speed_x
    ball_y_coord += ball_speed_y
        
    # 7. fill the screen with color
    screen.fill( black )

    # 9. drawing area
    
    # 10. define the player 1- left: a rectangle
    player_1 = pygame.draw.rect( screen, light_grey, ( player_1_x_coord, player_1_y_coord, player_width, player_height ) )

    # 10. define the player 2 - right
    player_2 = pygame.draw.rect( screen, light_grey, ( player_2_x_coord, player_2_y_coord, player_width, player_height ) )

    # 12. draw the ball
    ball = pygame.draw.circle( screen, light_grey, ( ball_x_coord, ball_y_coord ), ball_radius )
    
    # 14. center line
    pygame.draw.aaline( screen, light_grey, ( screen_width/2 ,0 ), ( screen_width/2, screen_height ) )

    # 13. collisions
    if ball.colliderect( player_1 ) or ball.colliderect( player_2 ):
        ball_speed_x *= -1

    # 8. refresh the windows
    pygame.display.flip()
    
    # 5. to refresh the screen
    clock.tick(60)