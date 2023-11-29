import pygame as pg
#import random
import sys
from settings import *
from player import *
from meteor import *
from map import *
from bullet import *
from explosion import *
from button import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()   
        self.screen = pg.display.set_mode(SCREEN)
        crear_tabla()
        self.list_show = []
        self.font = pg.font.SysFont("Arial", 100)
        self.void = ""
        self.user = ""
        self.aux = ""
        self.name_txt = ""
        self.flag_score = True
        self.flag_user = True
        self.flag_aux = True
        self.flag_show = True
        self.user_name = ""
        self.user_score = ""
        self.menu = True
        self.level = 0
        self.flag = True
        self.game_over = False
        self.easy = pg.image.load("image/easy.png").convert_alpha()
        self.easy = pg.transform.scale(self.easy, (200, 100))
        self.hard = pg.image.load("image/dificil.png").convert_alpha()
        self.hard = pg.transform.scale(self.hard, (200, 100))
        self.medium = pg.image.load("image/medio.png").convert_alpha()
        self.medium = pg.transform.scale(self.medium, (200, 100))
        self.impossible = pg.image.load("image/imposible.png").convert_alpha()
        self.impossible = pg.transform.scale(self.impossible, (200, 100))
        self.image_score = pg.image.load("image/score.png").convert_alpha()
        self.image_score = pg.transform.scale(self.image_score, (200, 100))
        self.score_button = Button(900, 100, self.image_score)
        self.easy_button = Button(100, 100, self.easy)
        self.hard_button = Button(500, 100, self.hard)
        self.medium_button = Button(100, 300, self.medium)
        self.impossible_button = Button(500, 300, self.impossible)
        self.clock = pg.time.Clock()
        self.sprite = pg.sprite.Group()
        self.meteor_list = pg.sprite.Group()
        self.bullet_list = pg.sprite.Group()
        self.player = Player()
        self.map = Map()
        self.sprite.add(self.player)
        self.score = 0
        pg.mixer.music.load("image/music.ogg")
        pg.mixer.music.set_volume(0.1)
        pg.mixer.music.play(loops=-1)
      
    def shoot(self):
        self.bullet = Bullet(self.player.rect.centerx, self.player.rect.top)  # Cambio realizado aquí
        self.sprite.add(self.bullet)
        self.bullet_list.add(self.bullet)

        laser_sound = pg.mixer.Sound("image/laser5.ogg")
        laser_sound.play()
    
    def check_collision(self):
        hits = pg.sprite.groupcollide(self.meteor_list, self.bullet_list, True, True)
        for hit in hits:
            explosion_sound = pg.mixer.Sound("image/explosion.wav")
            explosion_sound.play()
            self.score += 10
            explosion = Explosion(hit.rect.center)
            meteor = Meteor()
            self.sprite.add(explosion)
            self.sprite.add(meteor)
            self.meteor_list.add(meteor)
        
        hits = pg.sprite.spritecollide(self.player, self.meteor_list, True)
        for hit in hits:
            self.player.shield -= 25
            meteor = Meteor()
            self.sprite.add(meteor)
            self.meteor_list.add(meteor)
            if self.player.shield <= 0:
                self.game_over = True

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.check_collision()
            self.render()
    

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.shoot()
                if event.key == pg.K_SPACE:
                    self.void = self.void[0:-1]
                elif event.key == pg.K_RETURN:
                    self.user = self.aux
                    self.void = ""
                else:
                    self.void += event.unicode
                    self.aux = self.void

            #print(event)

    def update(self):
        self.clock.tick(FPS)
        fps = int(self.clock.get_fps())
        pg.display.set_caption("Game {0}".format(fps))
   
        self.sprite.update()
       

    def render(self):
        if self.game_over == False:
            self.screen.fill("white")
            map_scale = pg.transform.scale(self.map.image, SCREEN)
            self.screen.blit(map_scale, (0, 0))
            if self.menu == True:
                if self.easy_button.draw(self.screen):
                    self.level = 1
                    self.menu = False
                elif self.hard_button.draw(self.screen):
                    self.level = 2
                    self.menu = False
                elif self.medium_button.draw(self.screen):
                    self.level = 3
                    self.menu = False
                elif self.impossible_button.draw(self.screen):
                    self.level = 4
                    self.menu = False
                elif self.score_button.draw(self.screen):
                    self.level = 5
                    self.menu = False
            else:
                if self.level == 1:
                    if self.flag: 
                        for i in range(12):
                            self.meteor = Meteor()
                            self.sprite.add(self.meteor)
                            self.meteor_list.add(self.meteor)
                        self.flag = False
                    self.sprite.draw(self.screen)
                    self.map.render(self.screen, str(self.score), 25, 600, 10)
                    self.map.draw_shield(self.screen, 5, 5, self.player.shield)
                elif self.level == 2:
                    if self.flag:
                        for i in range(30):
                            self.meteor = Meteor()
                            self.sprite.add(self.meteor)
                            self.meteor_list.add(self.meteor)
                        self.flag = False
                    self.sprite.draw(self.screen)
                    self.map.render(self.screen, str(self.score), 25, 600, 10)
                    self.map.draw_shield(self.screen, 5, 5, self.player.shield)
                elif self.level == 3:
                    if self.flag:
                        for i in range(20):
                            self.meteor = Meteor()
                            self.sprite.add(self.meteor)
                            self.meteor_list.add(self.meteor)
                        self.flag = False
                    self.sprite.draw(self.screen)
                    self.map.render(self.screen, str(self.score), 25, 600, 10)
                    self.map.draw_shield(self.screen, 5, 5, self.player.shield)
                elif self.level == 4:
                    if self.flag:
                        for i in range(500):
                            self.meteor = Meteor()
                            self.sprite.add(self.meteor)
                            self.meteor_list.add(self.meteor)
                        self.flag = False
                    self.sprite.draw(self.screen)
                    self.map.render(self.screen, str(self.score), 25, 600, 10)
                    self.map.draw_shield(self.screen, 5, 5, self.player.shield)
                elif self.level == 5:
                    if self.flag_show:
                        self.list_show = show_data()
                        self.flag_show = False
                    for mensage in self.list_show:
                        name_score = mensage["data"]
                        pos_txt = mensage["pos_txt"]
                        for elemnt in name_score:
                            for element_2 in pos_txt:
                                ranking = elemnt
                                ranking_txt = self.font.render(ranking, True, "white")
                                self.screen.blit(ranking_txt, (120, element_2))


            pg.display.flip()        
        else:
            self.screen.fill("white")
            map_scale = pg.transform.scale(self.map.image, SCREEN)
            self.screen.blit(map_scale, (0, 0))
            self.text = self.font.render(str(self.score), True, "white")
            self.screen.blit(self.text, (600, 350))
            self.name_txt = self.font.render(self.void, True, "white")
            self.screen.blit(self.name_txt, (600, 450))
            if self.flag_score:
                self.user_score = str(self.score)
                self.flag_score = False
            if self.flag_user and self.user != "":
                self.user_name = str(self.user)
                self.flag_user = False
            if self.flag_score == False and self.flag_user == False:
                if self.flag_aux:
                    data_user(self.user_name, self.user_score)
                    self.flag_aux = False
            
        pg.display.flip()

game = Game()
game.run()
