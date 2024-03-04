class Helper:
        

    def flip_alex(sprites, x_flip):
        import pygame;
        flipped_sprites = []
        for sprite in sprites:
            flipped_sprites.append(pygame.transform.flip(sprite, x_flip, 0))
        return flipped_sprites