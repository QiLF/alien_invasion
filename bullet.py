import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    ''' A class for managing the bullets that the ship shoot'''
    def __init__(self, ai_settings, screen, ship):
        ''''''
        #super(Bullet, self).__init__()
        super().__init__()
        self.screen = screen
        # first create a rect for bullet, we'll set the correct position later on
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''move the bullet top'''
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        '''draw a bullet on the screen'''
        pygame.draw.rect(self.screen,self.color,self.rect)