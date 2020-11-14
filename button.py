import pygame
import os
class Button:
    text = ''
    width = 300
    height = 150
    x = 0
    y = 0 
    def __init__(self):
        self.sprite = pygame.image.load(os.path.join('button.png'))
        self.sprite = pygame.transform.scale(self.sprite,(self.width,self.height))

        
    def draw(self,screen,x,y):
        self.x = x
        self.y = y
        screen.blit(self.sprite,[x,y,self.width,self.height])
        font = pygame.font.SysFont("Nimbus Sans", 36)
        text = font.render(self.text, 200, (0, 0, 0))
        screen.blit(text, [x+60,y+35,15,25])
                

    def is_clicked(self,pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y+self.height 

