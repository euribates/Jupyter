#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
import math

import pygame

pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)

# Colores

black = (0, 0 , 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)



def random_color():
    return pygame.Color(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        255,
        )


class Point:

    def __init__(self, x=0, y=0, color=white):
        self.x = x
        self.y = y
        self.color = color

    @classmethod
    def random(self):
        x = random.randint(0, width)
        y = random.randint(0, width)
        color = random_color()
        return Point(x, y, color)

    def move(self):
        self.x += random.random() * 3 - 1.
        self.y += random.random() * 3 - 1.
        return self

    def distance(self, x, y):
        return (self.x - x)**2 + (self.y - y)**2
    
    def __repr__(self):
        return 'Point(x={}, y={}, color={})'.format(self.x, self.y, self.color)


points = [Point.random() for _ in range(2)]

def draw_voronoi(canvas, points):
    step = 5
    all_coords = (
        (x, y) 
        for x in range(0, width, step) 
        for y in range(0, height, step)
        )
    for x, y in all_coords:
        min_dist, centroide = min([(p.distance(x,y), p) for p in points], key=lambda t: t[0])
        pygame.draw.rect(canvas, centroide.color, (x-2, y-2, 5, 5))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            points.append(Point(x, y, random_color()))


    screen.fill(black)
    draw_voronoi(screen, points)
    for p in points:
        pygame.draw.rect(screen, white, (p.x-1, p.y-1, 2, 2))
        p.move()
    pygame.display.flip()

