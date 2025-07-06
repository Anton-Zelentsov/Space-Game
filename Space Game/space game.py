import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from statistics import Statistics
from rating import Scores
def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Космические войны')
    background_color = (0, 0, 0)
    lazer_gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_aliens(screen, aliens)
    statistics = Statistics()
    score = Scores(screen, statistics)
    while True:
        controls.events(screen, lazer_gun, bullets)
        if statistics.game_run:
            lazer_gun.update_lazer_gun()
            controls.update(background_color, screen, statistics, score ,lazer_gun, aliens, bullets)
            controls.update_bullets(screen, statistics, score, aliens, bullets)
            controls.update_aliens(statistics, screen, score, lazer_gun, aliens, bullets)

run()