from board import *

class Block(Board):

    def __init__(self):
        self.board = [[ 0 for x in xrange(columns)] for y in xrange(rows)]
        self.board += [[ 1 for x in xrange(columns)]]
        self.new_stone()
        self.level = 1
        self.score = 0
        self.lines = 0
        pygame.time.set_timer(pygame.USEREVENT+1, 900)

    def check_for_rotate(self):
        if not self.gameover and not self.paused:
                new_stone = self.rotate_clockwise(self.stone)
                if not self.check_collision(self.board, new_stone,(self.stone_x, self.stone_y)):
                        self.stone = new_stone

    def rotate_clockwise(self,shape):
            return [ [ shape[y][x]
                            for y in xrange(len(shape)) ]
                    for x in xrange(len(shape[0]) - 1, -1, -1) ]

    def move(self, delta_x):
            if not self.gameover and not self.paused:
                new_x = self.stone_x + delta_x
                if new_x < 0:
                        new_x = 0
                if new_x > columns - len(self.stone[0]):
                        new_x = columns - len(self.stone[0])
                if not self.check_collision(self.board,
                                       self.stone,
                                       (new_x, self.stone_y)):
                        self.stone_x = new_x
    def inst_fall(self):
            if not self.gameover and not self.paused:
                while(not self.fall(True)):
                   pass

    def new_stone(self):
            self.stone = self.next_stone[:]
            self.next_stone = blocks[rand(len(blocks))]
            self.stone_x = int(columns / 2 - len(self.stone[0])/2)
            self.stone_y = 0            
            if self.check_collision(self.board, self.stone,(self.stone_x, self.stone_y)):
                    self.gameover = True

