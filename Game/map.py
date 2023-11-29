import pygame as pg

class Map:
    def __init__(self) -> None:
        self.image = pg.image.load("image/background.png").convert_alpha()
    
    def render(self, screen, text, size, x, y):
        font = pg.font.SysFont("serif", size)
        text = font.render(text, True, "white")
        text_rect = text.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text, text_rect)
    
    def draw_shield(self, screen, x, y, percentage):
        lenght = 100
        height = 10
        fill = (percentage / 100) * lenght
        border = pg.Rect(x, y, lenght, height)
        fill = pg.Rect(x, y, fill, height)
        pg.draw.rect(screen, "green", fill)
        pg.draw.rect(screen, "white", border, 2)