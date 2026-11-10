import pygame
import random

# Set up the window
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Game")

# Player position
x = 275 
y = 175

# Falling block: position and speed
obj_x = random.randint(0, 570)
obj_y = 0
obj_speed = 4

# Score and lives
score = 0
lives = 3

# Clock (controls the speed) and font (for the text)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Game loop: runs about 60 times per second
running = True
while running:
    # Close the window when the player clicks X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Move the player with the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - 5
    if keys[pygame.K_RIGHT]:
        x = x + 5
    if keys[pygame.K_UP]:
        y = y - 5
    if keys[pygame.K_DOWN]:
        y = y + 5
        
    # Keep the player inside the window    
    if x < 0:
        x = 0
    if x > 550:
        x = 550
        
    if y < 0:
        y = 0
    if y > 350:
        y = 350
        
    # Move the falling block; if it reaches the bottom, the player loses a life
    obj_y = obj_y + obj_speed
    if obj_y > 400:
        lives = lives - 1
        obj_y = 0
        obj_x = random.randint(0,570)
        
    # Check if the player caught the block
    player_rect = pygame.Rect(x, y, 50, 50)
    obj_rect = pygame.Rect(obj_x, obj_y, 30, 30)
    if player_rect.colliderect(obj_rect):
        score = score + 1
        # Every 5 points the block falls faster
        if score % 5 == 0:
            obj_speed = obj_speed + 1
        obj_y = 0
        obj_x = random.randint(0, 570)
        pygame.display.set_caption("Score: " + str(score))
            
    # Draw everything on the screen
    screen.fill((0, 120, 0))
    pygame.draw.rect(screen, (255, 255, 0), (x, y, 50, 50))
    pygame.draw.rect(screen, (255, 0, 0), (obj_x, obj_y, 30, 30))
    text = font.render("Score:" + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    lives_text = font.render("Lives: " + str(lives), True, (255, 255, 255))
    screen.blit(lives_text, (10, 40))
    pygame.display.flip()
   
    # Game over when the lives run out
    if lives <= 0:
        over_text = font.render("GAME OVER - Score: " + str(score), True, (255, 255, 255))
        screen.blit(over_text, (150, 180))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
        
    clock.tick(60)
    
pygame.quit()