import pygame
from button import Button

class Intro:
    start_btn = Button()
    def draw(self,screen):
        font = pygame.font.Font(None, 36)
        text = font.render('Welcome to Slidding Puzzle Game', 100, (200, 200, 10))
        textpos = text.get_rect()
        screen.blit(text,(150,200))


        self.start_btn.text = "START GAME"
        self.start_btn.draw(screen,190,300)
