#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import pi
import pygame
import random
from pygame.locals import Rect
from vectores import Vector2

WIDTH, HEIGHT = SIZE = 800, 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30


def draw_vector(screen, color, a, b):
    pygame.draw.circle(screen, color, a, 3, 0)
    pygame.draw.line(screen, color, a, b, 1)
    left = b - a
    left = left.unit() * 10
    left.theta -= 7. * pi / 8.0
    pygame.draw.line(screen, color, b, b+left, 1)
    right = b - a
    right = right.unit() * 10
    right.theta += 7. * pi / 8.0
    pygame.draw.polygon(screen, color, [b, b+left, b+right, b], 0)


class Ball():
    def __init__(self, size):
        self.box = Rect((0, 0), size)
        self.pos = Vector2(*self.box.center)
        self.vel = Vector2.random_unit()
        self.speed = random.randrange(3, 10)
       
    def draw(self, canvas):
        pygame.draw.circle(canvas, (0, 0, 255), self.pos, 15)
        # traza
        draw_vector(canvas, GREEN, Vector2(0, 0), self.pos) 
        draw_vector(canvas, RED, self.pos, self.pos+self.vel*self.speed*10)
    
    def update(self):
        self.pos += self.vel * self.speed

    
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Rebotes")
    
    ball = Ball(SIZE)
    clock = pygame.time.Clock()
    in_game = True
    
    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
        
        ball.update()
        
        screen.fill(BLACK)
        ball.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
