#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import Rect
from vectores import Vector2

WIDTH, HEIGHT = SIZE = 800, 600
GREEN = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30

class Ball():
    def __init__(self, size):
        self.box = Rect((0, 0), size)
        self.pos = Vector2(*self.box.center)
        self.vel = Vector2.random_unit()
       
    def draw(self, canvas):
        pygame.draw.circle(self.image, (0, 0, 255), self.pos, 15) 
        pygame.draw.line(canvas, GREEN, (0, 0), self.pos)
    
    def update(self):
        self.pos += self.vel

        
    
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Rebotes")
    
    screen.fill(BLACK)
    ball = Ball(SIZE)
    clock = pygame.time.Clock()
    in_game = True
    
    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
        ball.update()
        ball.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
