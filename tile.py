import pygame
import random

class Tile(object):
    def __init__(self,number,x,y,width,height,image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = number
        self.image = image
    

    def draw(self,screen):
        if self.number == 1:
            pygame.draw.rect(screen,(255,255,255),[self.x,self.y,self.width,self.height])
        else:
            screen.blit(self.image,[self.x,self.y,self.width,self.height])
            self.draw_val(screen)

    def draw_val(self,screen):
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.number), 200, (200, 200, 10))
        textpos = text.get_rect()
        screen.blit(text, [self.x+self.width/2-7,self.y+self.height/2-12,15,25])

    def is_selected(self,pos):
        return self.x <= pos[0] <= self.x+self.width and self.y <= pos[1] <= self.y+self.height 


