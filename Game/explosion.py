import pygame as pg

class Explosion(pg.sprite.Sprite):
    def __init__(self, center) -> None:
        super().__init__()
        self.explosion = self.explosion_image()
        self.image = self.explosion[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.time = 50
    
    def explosion_image(self):
        explosion = []
        for i in range(9):
            file = "image/regularExplosion0{}.png".format(i)
            image = pg.image.load(file).convert()
            image.set_colorkey("black")
            image_scale = pg.transform.scale(image, (70, 70))
            explosion.append(image_scale)
        return explosion

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.time:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
