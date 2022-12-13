import pygame, controls
from gun import Gun
from pygame.sprite import Group

width = 854
height = 480


def go(width, height):
    '''
функция, которая запускает игру
    :param width: длина окна
    :param height: высота окна
    :return: движения на экране
    '''
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Стрелялка')
    back_image = pygame.image.load('image/back.png').convert()
    play = True
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    controls.do_army(screen, enemies)
    while play:
        controls.events(screen, gun, bullets)
        gun.move_gun()
        controls.kill_bul(bullets, screen, enemies)
        controls.update_screen(back_image, screen, gun, enemies, bullets)
        if len(enemies) == 0:
            play = False


go(width, height)
