#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import math
from PIL import Image, ImageDraw

green = (33, 233, 33)

class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vector({}, {})'.format(
            round(self.x, 10), 
            round(self.y, 10)
            )

    def __add__(self, other):
        return Vector(
            round(self.x + other.x, 10),
            round(self.y + other.y, 10),
            )
    
    def __mul__(self, num):
        return Vector(
            round(self.x * num),
            round(self.y * num),
            )

    def __eq__(self, other):
        return all([
            round(self.x, 10) == round(other.x, 10),
            round(self.y, 10) == round(other.y, 10),
            ])


right = Vector(1, 0)
left = Vector(-1, 0)
up = Vector(0, -1)
down = Vector(0, 1)


class Turtle(object):

    def __init__(self, size, pos=None):
        self.width, self.height = size
        self.img = Image.new('RGB', size, color=(33,33,33))
        self.head = right
        self.pos = pos or Vector(self.width // 2, self.height // 2)
        self.set_angle(math.pi / 2.0)
        self.stack = []

    def push(self):
        self.stack.append((
            self.pos,
            self.head,
            ))

    def pop(self):
        if self.stack:
            self.pos, self.head = self.stack.pop()

    def get_angle(self):
        print('get_angle called')
        return self._angle

    def set_angle(self, angle):
        print('set_angle called')
        self._angle = angle
        sin_theta = round(math.sin(angle), 10)
        cos_theta = round(math.cos(angle), 10)
        self.rot = [
            [cos_theta, -sin_theta],
            [sin_theta,  cos_theta],
            ]

    angle = property(get_angle, set_angle)

    def left(self):
        self.head = Vector(
            self.head.x * self.rot[0][0] + self.head.y * self.rot[1][0],
            self.head.x * self.rot[0][1] + self.head.y * self.rot[1][1],
            )

    def right(self):
        self.head = Vector(
            self.head.x * self.rot[0][0] - self.head.y * self.rot[1][0],
            - self.head.x * self.rot[0][1] + self.head.y * self.rot[1][1],
            )

    def forward(self, size=1):
        pos = self.pos
        new_pos = pos + self.head * size
        draw = ImageDraw.Draw(self.img)
        lines = [
            (pos.x, pos.y),
            (new_pos.x, new_pos.y)
            ]
        draw.line(lines, green)
        self.pos = new_pos

    def jump(self):
        self.pos = self.pos + self.head

