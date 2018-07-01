import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        # initialize the ship and set its position
        self.screen = screen
        # load ship.bmp
        self.image = pygame.image.load('images/ship.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        # set every new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #
        self.center = float(self.rect.centerx)
        # flag for moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        ''' adjust the position of the ship due to the moving flag'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update the centerx due to center
        self.rect.centerx = self.center

    def blitme(self):
        # show the ship in the correct position
        self.screen.blit(self.image, self.rect)
