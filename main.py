import sys, pygame
import time 
import os
from board import Board
from game import Game
from intro import Intro

def main():
    pygame.init()

    size = width, height = 720, 700
    black = (0, 0, 0)
    screen = pygame.display.set_mode(size)

    running = True

    bd = Board(3)
    intro = Intro()
    game = Game(0) # 0 -> intro menu, 1 ->game

    while running:

        screen.fill(black)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: #exit condition
                running = False
            # check for mouse positions for intro menu
            if game.state == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if intro.start_btn.is_clicked(pos):
                        game.state = 1 #starts the game


            # check for mouse positions for the main game  
            if game.state == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    initial_pos = pygame.mouse.get_pos()
                    tile = bd.get_selected_tile(initial_pos)

                    if bd.solve_btn.is_clicked(initial_pos):
                        bd.is_solving = True
                        bd.solve_puzzle()

                if event.type == pygame.MOUSEBUTTONUP:
                    if tile != None:
                        final_pos = pygame.mouse.get_pos()
                        direction = bd.drag_direction(initial_pos, final_pos)
                        bd.move_tile(tile,direction)

        
        if game.state == 0:
            intro.draw(screen)
        else:
            if bd.is_solving == True:
                bd.walk_path(bd.solving_path)
                bd.draw(screen)
                time.sleep(0.3) # solving speed
            else:
                bd.draw(screen)
            
        pygame.display.update()

    
    pygame.display.quit()
    pygame.quit()
    


if __name__ == '__main__':
    main()
      

