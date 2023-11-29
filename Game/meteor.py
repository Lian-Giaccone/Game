import pygame as pg
import random

class Meteor(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.meteor = self.meteor_image()
        self.image = random.choice(self.meteor)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1200 - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 10)
        self.speed_x = random.randrange(-5, 5)
    
    def meteor_image(self):
        images = []
        list = ["image/meteorGrey_big1.png", "image/meteorGrey_big2.png", "image/meteorGrey_big3.png", "image/meteorGrey_big4.png",
				"image/meteorGrey_med1.png", "image/meteorGrey_med2.png", "image/meteorGrey_small1.png", "image/meteorGrey_small2.png",
				"image/meteorGrey_tiny1.png", "image/meteorGrey_tiny2.png"]
        for img in list:
            images.append(pg.image.load(img).convert_alpha())
        return images

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top > 700 + 10 or self.rect.left < -25 or self.rect.right > 1200 + 22:
            self.rect.x = random.randrange(1200 - self.rect.width)
            #self.rect.y = random.randrange(-100, -40)
            #self.speed_y = random.randrange(1, 8)

            self.rect.y = random.randrange(-150, -100)
            self.speed_y = random.randrange(1, 8)
            