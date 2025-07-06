import pygame
import sys
from bullet import Bullet
from aliens import Aliens
import time
def events(screen, lazer_gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Вправо
            if event.key == pygame.K_d:
                lazer_gun.move_right = True
            elif event.key == pygame.K_a:
                lazer_gun.move_left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, lazer_gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # Вправо
            if event.key == pygame.K_d:
                lazer_gun.move_right = False
            elif event.key == pygame.K_a:
                lazer_gun.move_left = False

def update(background_color, screen, statistics, score, lazer_gun, aliens, bullets):
    screen.fill(background_color)
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    lazer_gun.output()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(screen, statistics, score, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            statistics.score += 10 * len(aliens)
        score.image_score()
        check_best_score(statistics, score)
        score.image_lives()
    if len(aliens) == 0:
        bullets.empty()
        create_aliens(screen, aliens)

def lazer_gun_kill(statistics, screen, score, lazer_gun, aliens, bullets):
    if statistics.lazer_gun_life > 0:
        statistics.lazer_gun_life -= 1
        score.image_lives()
        aliens.empty()
        bullets.empty()
        create_aliens(screen, aliens)
        lazer_gun.create_lazer_gun()
        time.sleep(1)
    else:
        statistics.game_run = False
        sys.exit()

def update_aliens(statistics, screen, score, lazer_gun, aliens, bullets):
    aliens.update()
    if pygame.sprite.spritecollideany(lazer_gun, aliens):
        lazer_gun_kill(statistics, screen, score, lazer_gun, aliens, bullets)
    aliens_check(statistics, screen, score, lazer_gun, aliens, bullets)

def aliens_check(statistics, screen, score, lazer_gun, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            lazer_gun_kill(statistics, screen, score, lazer_gun, aliens, bullets)
            break

def create_aliens(screen, aliens):
    alien = Aliens(screen)
    alien_width = alien.rect.width
    number_aliens_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_aliens_y = int((800 - 100 - 2 * alien_height) / alien_height)
    for row_number in range(number_aliens_y - 1):
        for aliens_number in range(number_aliens_x):
            alien = Aliens(screen)
            alien.x = alien_width + (alien_width * aliens_number)
            alien.y = alien_height + (alien_height * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * row_number)
            aliens.add(alien)

def check_best_score(statistics, score):
    if statistics.score > statistics.best_score:
        statistics.best_score = statistics.score
        score.image_best_score()
        with open('Best record', 'w') as f:
            f.write(str(statistics.best_score))