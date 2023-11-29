import pygame as pg

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pg.image.load("image/laser1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()