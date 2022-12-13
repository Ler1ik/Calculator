import pygame


class Bullet(pygame.sprite.Sprite):
    '''
    класс пуль
    '''

    def __init__(self, screen, gun):
        '''
        инифиальзация пули
        :param screen: экран
        :param gun: расположение пушки
        '''
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 15, 6)
        self.color = 123, 154, 0
        self.speed = 0.6
        self.rect.centery = gun.rect.centery
        self.rect.right = gun.rect.right
        self.x = float(self.rect.x)

    def update(self):
        '''
        обновление положения пули относительно точки, от которой она была отправлена
        :return: число на оси, где находится пуля
        '''
        self.x += self.speed
        self.rect.x = self.x

    def draw_bul(self):
        '''
        отрисовка пули
        :return: пуля на экране
        '''
        pygame.draw.rect(self.screen, self.color, self.rect)
