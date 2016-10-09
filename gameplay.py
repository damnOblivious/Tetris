#!/usr/bin/env python2
from random import randrange as rand
import pygame, sys
from block import *

class Gameplay(Block):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(str(rollno) +'_Tetris')
        pygame.key.set_repeat(250,25)
        self.width = cell_size*(columns+10)
        self.height = cell_size*rows
        self.score_board = cell_size*columns
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.default_font =  pygame.font.Font(pygame.font.get_default_font(), 16)
        self.next_stone = blocks[rand(7)]       
        Block.__init__(self)

    def begin(self):
        if self.gameover:
                Block.__init__(self)
                self.gameover = False

    def disp_msg(self, msg, topleft):
        x,y = topleft
        for line in msg.splitlines():
                self.screen.blit(self.default_font.render(line,False,white,black),(x,y))
                y+=14
        
    def center_msg(self, msg):
        for i, line in enumerate(msg.splitlines()):
                msg_image =  self.default_font.render(line, False,white,black)
        
                msgim_center_x, msgim_center_y = msg_image.get_size()
                msgim_center_x //= 2
                msgim_center_y //= 2
        
                self.screen.blit(msg_image, (
                  self.width // 2-msgim_center_x,
                  self.height // 2-msgim_center_y+i*22))

    def pause(self):
        self.paused = not self.paused
  
    def quit(self):
        self.center_msg("Aborting...")
        pygame.display.update()
        sys.exit() 



    def lets_begin(self):
        self.gameover = self.paused = False
        user_controls = {
                    'ESCAPE':   self.quit,
                    'a':        lambda:self.move(-1),
                    'd':        lambda:self.move(+1),
                    'DOWN':     lambda:self.fall(True),
                    's':        self.check_for_rotate,
                    'p':        self.pause,
                    'n':        self.begin,
                    'SPACE':    self.inst_fall
        }
        
        while True:
                self.screen.fill(game_area)
                pygame.draw.rect(self.screen,side_menu,[(columns)*cell_size,0,
                    (columns+10)*cell_size,(rows)*cell_size],0)
                if self.gameover:
                        self.center_msg("""Sorry !! bye bye !\n
                                Total Score: %d Press "n to continue""" % self.score)
                else:
                        if self.paused:
                                self.center_msg("Paused")
                        else:
                                pygame.draw.line(self.screen,red,(self.score_board+1, 0),(self.score_board+1, self.height-1))
                                self.disp_msg("Total: %d\n\nLevel: %d" % (self.score, self.level),
                                        (self.score_board+cell_size, cell_size*5))
                                self.draw_matrix(self.board, (0,0))
                                self.draw_blocks(self.stone,(self.stone_x, self.stone_y))
                pygame.display.update()
                
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                for key in user_controls:
                                        if event.key == eval("pygame.K_"+key):
                                                user_controls[key]()
                        elif event.type == pygame.QUIT:
                                self.quit()
                        elif event.type == pygame.USEREVENT+1:
                                self.fall(False)
                

newgame=Gameplay()
newgame.lets_begin()
