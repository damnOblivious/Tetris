from random import randrange as rand
import pygame, sys

########################################
rollno=201502166
rows =      30
columns =      32
cell_size = 22
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
side_menu=(255,182,193)
game_area=(245,245,220)
blocks_color=(100,149,237)

blocks = [
        [[1, 1, 1],
         [0, 1, 0]],
        
        [[0, 1, 1],
         [1, 1, 0]],
        
        [[1, 1, 0],
         [0, 1, 1]],
        
        [[1, 0, 0],
         [1, 1, 1]],
        
        [[0, 0, 1],
         [1, 1, 1]],
        
        [[1, 1, 1, 1]],
        
        [[1, 1],
         [1, 1]]
]


########################################


class Board():
    def draw_blocks(self,matrix,offset):
        off_x, off_y  = offset
        for y, row in enumerate(matrix):
                for x, val in enumerate(row):
                        if val:
                                pygame.draw.rect(self.screen,black,pygame.Rect((off_x+x)*cell_size,(off_y+y) * cell_size,cell_size,cell_size),1)

    def draw_matrix(self,matrix,offset):
        off_x, off_y  = offset
        for y, row in enumerate(matrix):
                for x, val in enumerate(row):
                        if val:
                                pygame.draw.rect(self.screen,blocks_color,pygame.Rect((off_x+x)*cell_size,(off_y+y) * cell_size,cell_size,cell_size),0)
  
    def check_collision(self,board, shape, offset):
            off_x, off_y = offset
            for cy, row in enumerate(shape):
                    for cx, cell in enumerate(row):
                            try:
                                    if cell and board[ cy + off_y ][ cx + off_x ]:
                                            return True
                            except IndexError:
                                    return True
            return False
    
    def add_cl_lines(self, n):
       linescores = [0, 40, 100, 300, 1200]
       self.lines += n
       self.score += linescores[n] * self.level
       if self.lines >= self.level*6:
               self.level += 1
               newdelay = 900-150*(self.level-1)
               newdelay = 100 if newdelay < 100 else newdelay
               pygame.time.set_timer(pygame.USEREVENT+1, newdelay)   
 
    def row_remove(self,board, row):
        del board[row]
        return [[0 for i in xrange(columns)]] + board

    def join_matrixes(self,mat1, mat2, mat2_off):
            off_x, off_y = mat2_off
            for cy, row in enumerate(mat2):
                    for cx, val in enumerate(row):
                            mat1[cy+off_y-1 ][cx+off_x] += val
            return mat1

    def fall(self, manual):
            if not self.gameover and not self.paused:
                    self.score += 1 if manual else 0
                    self.stone_y += 1
                    if self.check_collision(self.board,self.stone,(self.stone_x, self.stone_y)):
                            self.board = self.join_matrixes(self.board,self.stone,(self.stone_x, self.stone_y))
                            self.new_stone()
                            cleared_rows = 0
                            while True:
                                    for i, row in enumerate(self.board[:-1]):
                                            if 0 not in row:
                                                    self.board = self.row_remove(self.board, i)
                                                    cleared_rows += 1
                                                    break
                                    else:
                                            break
                            self.add_cl_lines(cleared_rows)
                            return True
            return False
