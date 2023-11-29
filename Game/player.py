import pygame as pg
from bullet import *

class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pg.image.load("image/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 600
        self.rect.bottom = 690
        self.speed = 0
        self.shield = 100
    
    def update(self):
        self.speed = 0
        key = pg.key.get_pressed()
        
        if key[pg.K_a]:
            self.speed = -7
        if key[pg.K_d]:
            self.speed = 7

        self.rect.x += self.speed

        if self.rect.right > 1200:
            self.rect.right = 1200
        if self.rect.left < 0:
            self.rect.left = 0
    
        