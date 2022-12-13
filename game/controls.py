import pygame
from bullets import Bullet
from enemy import Enemy


def events(screen, gun, bullets):
    for doings in pygame.event.get():
        if doings.type == pygame.QUIT:
            quit()
        elif doings.type == pygame.KEYDOWN:
            if doings.key == pygame.K_s:
                gun.high = True
            elif doings.key == pygame.K_w:
                gun.low = True
            elif doings.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif doings.type == pygame.KEYUP:
            if doings.key == pygame.K_s:
                gun.high = False
            elif doings.key == pygame.K_w:
                gun.low = False


def update_screen(back_image, screen, gun, enemies, bullets):
    screen.blit(back_image, [0, 0])
    for bullet in bullets.sprites():
        bullet.draw_bul()
    gun.output()
    enemies.draw(screen)
    pygame.display.flip()


def kill_bul(bullets, screen, enemies):
    bullets.update()
    screen_rect = screen.get_rect()
    for bullet in bullets.copy():
        if bullet.rect.left >= screen_rect.right:
            bullets.remove(bullet)
    pygame.sprite.groupcollide(bullets, enemies, True, True)


def do_army(screen, enemies):
    enemy = Enemy(screen)
    enemy_height = enemy.rect.height
    number_enemy_y = int((480 - 2 * enemy_height) / enemy_height + 1)

    for enemy_number in range(number_enemy_y):
        enemy = Enemy(screen)
        enemy.y = enemy_height + enemy_height * enemy_number
        enemy.rect.y = enemy.y
        enemies.add(enemy)
