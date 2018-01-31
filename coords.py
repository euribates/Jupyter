#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
import math

import pygame

pygame.init()

size = width, height = 640, 480
center = offset_x, offset_y = width // 2, height // 2
zoom = 20
screen = pygame.display.set_mode(size)



# Colores

black = (0, 0 , 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (51, 102, 255)
yellow = (255, 255, 0)
silver = (102, 102, 102)

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

    def scale(self):
        x, y = self.x, self.y
        x = offset_x + x*zoom
        y = offset_y - y*zoom
        return int(round(x)), int(round(y))

    def move(self):
        self.x += random.random() / 20.0 - 0.025
        self.y += random.random() / 20.0 - 0.025
        return self

    def distance(self, x, y):
        return (self.x - x)**2 + (self.y - y)**2
    
    def __repr__(self):
        name = self.__class__.__name__
        return '{}(x={}, y={}, color={})'.format(
            name, self.x, self.y, self.color
            )

    def draw(self, canvas):
        x, y = self.scale()
        canvas.set_at((x, y), self.color)    # The point itself
        canvas.set_at((x-1, y), self.color)  # cross
        canvas.set_at((x+1, y), self.color)
        canvas.set_at((x, y-1), self.color)
        canvas.set_at((x, y+1), self.color)

    @classmethod
    def random(self):
        x = random.randint(0, width)
        y = random.randint(0, width)
        color = random_color()
        return Point(x, y, color)


class Triangle(Point):

    def draw(self, canvas):
        x, y = self.scale()
        vertices = [
            (x-4, y+4),
            (x, y-4),
            (x+4, y+4)
            ]
        pygame.draw.polygon(canvas, self.color, vertices, 0)


class Circle(Point):

    def draw(self, canvas):
        x, y = self.scale()
        pygame.draw.circle(canvas, self.color, (x,y), 6, 0)


class Square(Point):

    def draw(self, canvas):
        x, y = self.scale()
        pygame.draw.rect(canvas, self.color, (x-4, y-4, 9, 9))



points = [
    Circle(3, 4, red),
    Circle(5, -3, green),
    Circle(-2, 5, blue),
    Circle(-4, 2, yellow),
   
    Square(2, -2, red),
    Square(-1, -5, green),
    Square(-3, -2, blue),
    Square(4, 0, yellow),

    Triangle(-5, 0, red),
    Triangle(0, 6, green),
    Triangle(0, -3, blue),
    Triangle(0, 0, yellow),
    ]

def draw_axis(screen):
    pygame.draw.line(screen, silver, (0, offset_y), (width, offset_y)) 
    for step in range(0, width, zoom):
        pygame.draw.line(screen, silver,
            (step, offset_y-2),
            (step, offset_y+2)
            ) 
    for step in range(0, height, zoom):
        pygame.draw.line(screen, silver,
            (offset_x-2, step),
            (offset_x+2, step)
            ) 

    pygame.draw.line(screen, silver, (offset_x, 0), (offset_x, height)) 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            x = int(round((x - offset_x) / zoom))
            y = -int(round((y - offset_y) / zoom))
            print(x, y)
            Shape = random.choice([Square, Triangle, Circle])
            points.append(Shape(x, y, random_color()))

    screen.fill(black)
    draw_axis(screen)
    for p in points:
        p.move()
        p.draw(screen)
    pygame.display.flip()

