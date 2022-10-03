# 1. initialize pygame
import pygame
pygame.init()

# 2. colors variables
black = ( 0, 0, 0 )
white = ( 255, 255, 255 )

# 3. screen size
screen_size = ( 800,600 )

# 11. define the player constants
player_width = 15
player_height = 90

# 11.1 Coordinates player 1
player_1_x_coord = 50
player_1_y_coord = 300 - ( player_height / 2 )
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
                player_1_y_speed = -20

            if event.key == pygame.K_s:
                player_1_y_speed = 20
            
            # 13.2 player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = -20

            if event.key == pygame.K_DOWN:
                player_2_y_speed = 20
        
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

    # ball limits
    if ball_y_coord > 590 or ball_y_coord < 10:
        ball_speed_y *= -1

    # ball boundary: right or left
    if (ball_x_coord > 800) or (ball_x_coord < 0):
        ball_x_coord = 400
        ball_y_coord = 300

        ball_speed_x *= -1
        ball_speed_y *= -1
    

    # players and ball movement
    player_1_y_coord += player_1_y_speed
    player_2_y_coord += player_2_y_speed
    # ball movement
    ball_x_coord += ball_speed_x
    ball_y_coord += ball_speed_y
        
    # 7. fill the screen with color
    screen.fill( black )

    # 9. drawing area
    
    # 10. define the player 1- left: a rectangle
    player_1 = pygame.draw.rect( screen, white, ( player_1_x_coord, player_1_y_coord, player_width, player_height ) )

    # 10. define the player 2 - right
    player_2 = pygame.draw.rect( screen, white, ( player_2_x_coord, player_2_y_coord, player_width, player_height ) )

    # 12. draw the ball
    ball = pygame.draw.circle( screen, white, ( ball_x_coord, ball_y_coord ), ball_radius )

    # 13. collisions
    if ball.colliderect( player_1 ) or ball.colliderect( player_2 ):
        ball_speed_x *= -1

    # 8. refresh the windows
    pygame.display.flip()
    
    # 5. to refresh the screen
    clock.tick(60)
pygame.quit()