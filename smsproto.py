import pygame
from helper import Helper
from spritesheet import SpriteSheet

pygame.init()

screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
running = True
player_pos = (20, 20)

real_resolution_surface = pygame.Surface((256, 192))

filename = "media/8622.png"
alex_sprites = SpriteSheet(filename)    
player_run1 = alex_sprites.image_at((8, 8, 16, 32), (186,254,202)) 
player = alex_sprites.image_at((32, 8, 16, 32), (186,254,202)) 
player_run2 = alex_sprites.image_at((56, 8, 16, 32), (186,254,202)) 

run_sequence = 1
run_direction = 1
player_walk = list(map(Helper.flip_alex, (player_run2, player, player_run1 ), (run_direction, run_direction, run_direction)))
while running:
        # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        pygame.key.set_repeat(1, 60)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:            
            player_pos = (player_pos[0] + 3, player_pos[1])
            run_sequence = (run_sequence + 1) % 3
            run_direction = 1
            player_walk = list(map(Helper.flip_alex, (player_run2, player, player_run1 ), (run_direction, run_direction, run_direction)))
        if keys[pygame.K_LEFT]:            
            player_pos = (player_pos[0] - 3, player_pos[1])
            run_sequence = (run_sequence + 1) % 3
            run_direction = 0
            player_walk = list(map(Helper.flip_alex, (player_run2, player, player_run1 ), (run_direction, run_direction, run_direction)))
        if keys.count == 0:
                run_sequence = 1            
    
    screen.fill("black")
    real_resolution_surface.fill("orange")
    
    real_resolution_surface.blit(player_walk[run_sequence], player_pos)
    
    screen.blit(pygame.transform.scale(real_resolution_surface, screen.get_size()), (0,0))        

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()






