#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# vectores.py

import pygame
import random
from math import sin, cos, atan2, sqrt, pi

class Vector2(object):

    def __init__(self, x, y=None):
        if y is None:  # Created using a tuple or list
            self.x = float(x[0])
            self.y = float(x[1])
        else:
            self.x = float(x)
            self.y = float(y)
    
    def __str__(self):
        return 'Vector2({}, {})'.format(self.x, self.y)

    __repr__ = __str__

    def _get_theta(self):
            return atan2(self.y, self.x)

    def _set_theta(self, v):
        m = self.mod
        self.x = round(m * cos(v), 9)
        self.y = round(m * sin(v), 9)

    theta = property(_get_theta, _set_theta)

    @property
    def mod(self):
        return round(sqrt(self.x**2 + self.y**2), 9)

    def unit(self):
        m = self.mod
        return Vector2(self.x / m, self.y / m)

    def as_tuple(self): 
        return (int(round(self.x)), int(round(self.y)))

    def turn_left(self):
        return Vector2(-self.y, self.x)

    def turn_right(self):
        return Vector2(self.y, -self.x)

    def __add__(self, op2):
        return Vector2(self.x + op2[0], self.y + op2[1])

    def __sub__(self, op2):
        return Vector2(self.x - op2.x, self.y - op2.y)

    def __mul__(self, op2):
        return Vector2(self.x * op2, self.y * op2)

    def __div__(self, op2):
        return Vector2(self.x / op2, self.y / op2)

    def __matmul__(self, op2):
        return self.x * op2.x + self.y * op2.y

    def __eq__(self, op2):
        return self.x == op2.x and self.y == op2.y

    def __iter__(self):
        self._index = 0
        return self

    def next(self):
        if self._index == 0:
            self._index = 1
            return int(round(self.x))
        elif self._index == 1:
            self._index = 2
            return int(round(self.y))
        else:
            raise StopIteration

    def __getitem__(self, index):
        if index == 0:
            return int(round(self.x))
        elif index == 1:
            return int(round(self.y))
        else:
            raise KeyError('El indice {} no es correcto'.format(index))

    def __len__(self):
        return 2

    @staticmethod
    def random(max_x, max_y):
        return Vector2(
            random.randrange(0, max_x),
            random.randrange(0, max_y),
            )
    
    @staticmethod
    def Up(): return Vector2(0, -1)

    @staticmethod
    def Down(): return Vector2(0, 1)

    @staticmethod
    def Left(): return Vector2(-1, 0)

    @staticmethod
    def Right(): return Vector2(1, 0)

    @staticmethod
    def Zero(): return Vector2(0, 0)

    @staticmethod
    def random_unit():
        angle = random.uniform(0, 2 * pi)
        return Vector2(cos(angle), sin(angle))



