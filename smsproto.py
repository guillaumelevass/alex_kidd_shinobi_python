import pygame
from helper import Helper
from spritesheet import SpriteSheet

pygame.init()

screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
running = True
player_pos = (20, 20)
animation_beat = 3

real_resolution_surface = pygame.Surface((256, 192))

filename = "media/8622.png"
alex_sprites = SpriteSheet(filename)    
player_run1 = alex_sprites.image_at((8, 8, 16, 32), (186,254,202)) 
player = alex_sprites.image_at((32, 8, 16, 32), (186,254,202)) 
player_run2 = alex_sprites.image_at((56, 8, 16, 32), (186,254,202)) 

player_atk1 = alex_sprites.image_at((8, 57, 16, 32), (186,254,202)) 
player_atk2 = alex_sprites.image_at((71, 48, 16, 48), (186,254,202)) 
player_atk3 = alex_sprites.image_at((31, 48, 33, 48), (186,254,202))
player_atk4 = alex_sprites.image_at((95, 48, 33, 48), (186,254,202))
player_atk5 = alex_sprites.image_at((135, 48, 33, 48), (186,254,202)) 

player_anim = []

run_sequence = 0
run_direction = 1
player_walk = [player, player_run1, player_run2]
player_atk = [player_atk1, player_atk2, player_atk3, player_atk4, player_atk5]
player_anim = player_walk
current_animation_beat = 0
player_atk_counter = 0
frame_id = 0
is_atk = False
atk_sequence = 0
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
            if (current_animation_beat % animation_beat == 0):
                run_sequence = (run_sequence + 1) % animation_beat
            run_direction = 1
            player_anim = Helper.flip_alex(player_walk, run_direction)
        if keys[pygame.K_LEFT]:            
            player_pos = (player_pos[0] - 3, player_pos[1])
            if (current_animation_beat % animation_beat == 0):
                run_sequence = (run_sequence + 1) % animation_beat
            run_direction = 0           
            player_anim = Helper.flip_alex(player_walk, run_direction)
        if keys[pygame.K_SPACE]:            
            player_anim = Helper.flip_alex(player_atk, run_direction)
            is_atk = True
            current_animation_beat = 0
        if keys.count == 0:
                player_anim = Helper.flip_alex(player_walk, run_direction)
                run_sequence = 1
        current_animation_beat = current_animation_beat + 1   
        if is_atk:
            if (current_animation_beat % animation_beat == 0):
                if atk_sequence == 4:
                    is_atk = False
                    run_sequence = 0
                    current_animation_beat = 0
                atk_sequence = (atk_sequence + 1) % 5
                
            
               
    
    screen.fill("black")
    real_resolution_surface.fill("orange")
    
    if is_atk: # replace with one big list and change offset
        player_anim = Helper.flip_alex(player_atk, run_direction)
        run_sequence = atk_sequence

    real_resolution_surface.blit(player_anim[run_sequence], player_pos)
    frame_id = frame_id + 1

    screen.blit(pygame.transform.scale(real_resolution_surface, screen.get_size()), (0,0))        

    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()







