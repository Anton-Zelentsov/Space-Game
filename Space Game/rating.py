import pygame.font
from gun import Gun
from pygame.sprite import Group

class Scores():
    def __init__(self, screen, statistics):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.statistics = statistics
        self.text_color = (245, 228, 156)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_best_score()
        self.image_lives()

    def image_score(self):
        self.score_image = self.font.render(str(self.statistics.score), True, self.text_color, (0, 0, 0))
        self.rect_score = self.score_image.get_rect()
        self.rect_score.right = self.screen_rect.right - 40
        self.rect_score.top = 20

    def image_best_score(self):
        self.best_score_image = self.font.render(str(self.statistics.best_score), True, self.text_color, (0,0,0))
        self.best_score_rect = self.best_score_image.get_rect()
        self.best_score_rect.centerx = self.screen_rect.centerx
        self.best_score_rect.top = self.screen_rect.top + 20

    def image_lives(self):
        self.lives = Group()
        for live_number in range(self.statistics.lazer_gun_life):
            live = Gun(self.screen)
            live.rect.x = 15 + live_number * live.rect.width
            live.rect.y = 20
            self.lives.add(live)

    def show_score(self):
        self.screen.blit(self.score_image, self.rect_score)
        self.screen.blit(self.best_score_image, self.best_score_rect)
        self.lives.draw(self.screen)
