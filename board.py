from tile import Tile
from button import Button
from solver import Solver
import pygame
import os
import random


class Board(object):
    tiles = []
    solving_path = []
    solve_btn = Button()

    is_solving = False

    
    def __init__(self, number_of_tiles):
        oimag = pygame.image.load(os.path.join('wallhaven-506949.jpg'))
        oimag = pygame.transform.scale(oimag, (number_of_tiles*100,number_of_tiles*100))
        
        self.number_of_tiles = number_of_tiles
        number = 0 
        for i in range(number_of_tiles):
            self.tiles.append([])
            for j in range(number_of_tiles):
                number += 1
                cropped = pygame.Surface((100, 100))
                cropped.blit(oimag, (0, 0), (100*j, 100*i, 100, 100))
                self.tiles[i].append(Tile(number,200+110*j,50+110*i,100,100,cropped))

    def draw_buttons(self,screen):
        self.solve_btn.text = 'Solve Puzzle'
        self.solve_btn.draw(screen,200,self.number_of_tiles*100+100+self.solve_btn.height)

    def draw(self,screen):
        self.draw_buttons(screen)

        for row in self.tiles:
            for tile in row:
                tile.draw(screen)
                tile.draw_val(screen)

    def get_selected_tile(self,pos):
        for row in self.tiles:
            for tile in row:
                if tile.is_selected(pos):
                    return tile
        return None
        
    def drag_direction(self,initial_pos, final_pos)->str:
        if abs(initial_pos[0]-final_pos[0]) > abs(initial_pos[1]-final_pos[1]):
            # horizontal movement
            if initial_pos[0] > final_pos[0]:
                return 'L' # left
            else:
                return 'R' # right

        else:
            # vertical movement
            if initial_pos[1] > final_pos[1]:
                return 'U' # up
            else:
                return 'D' # down

    def move_tile(self,curr_tile,direction):
        if curr_tile is None:
            return 
        pos = {
            "D" :  (1,  0),
            "U" : (-1,  0),
            "L" :  (0, -1),
            "R" :  (0,  1),
        }

        for i,row in enumerate(self.tiles):
            for j,tile in enumerate(row):
                if tile.number == curr_tile.number:
                    query_x = i+pos[direction][0]
                    query_y = j+pos[direction][1]
                    if (0 <= query_x < self.number_of_tiles) and (0 <= query_y < self.number_of_tiles):
                        if self.tiles[query_x][query_y].number == 1:
                            self.tiles[query_x][query_y].number, self.tiles[i][j].number =  self.tiles[i][j].number, self.tiles[query_x][query_y].number
                            self.tiles[query_x][query_y].image, self.tiles[i][j].image =  self.tiles[i][j].image, self.tiles[query_x][query_y].image
                            return



    def walk_path(self,path):
        pos = {
            "D" :  (1,  0),
            "U" :  (-1, 0),
            "L" :  (0, -1),
            "R" :  (0,  1),
        }

        if len(path) != 0:
            for i,row in enumerate(self.tiles):
                for j,tile in enumerate(row):
                    if tile.number == 1:            
                        query_x = i+pos[path[0]][0]
                        query_y = j+pos[path[0]][1]
                        path.pop(0)
                        self.tiles[query_x][query_y].number, self.tiles[i][j].number =  self.tiles[i][j].number, self.tiles[query_x][query_y].number
                        self.tiles[query_x][query_y].image, self.tiles[i][j].image =  self.tiles[i][j].image, self.tiles[query_x][query_y].image
                        break
                        break
        else:
            self.is_solving = False


    def solve_puzzle(self):
        slv = Solver()
        mat_init = []
        mat_fin = []

        for i,row in enumerate(self.tiles):
            mat_init.append([x.number for x in row])
        
        k = 1
        for i in range(self.number_of_tiles):
            mat_fin.append([x for x in range(k,k+self.number_of_tiles)])
            k += self.number_of_tiles

        mat_init = Solver.convert_to_tuple(mat_init) #performancewise
        mat_fin = Solver.convert_to_tuple(mat_fin)


        path = Solver.decrypt_path(slv.solve(mat_init,mat_fin,self.number_of_tiles),self.number_of_tiles)
        self.solving_path = list(path)




        
