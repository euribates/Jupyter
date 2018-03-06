#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import pytest
import random
import math
import tortuga
from tortuga import Vector, Turtle

def test_vector_equal():
    assert Vector(0, 0) == Vector(0, 0)
    assert Vector(0, 0) != Vector(0, 1)

def test_left():
    t = tortuga.Turtle((500, 500))
    assert t.head == tortuga.right
    print(t.head, tortuga.up, t.head == tortuga.up, t.rot)
    t.left()
    print(t.head, tortuga.up, t.head == tortuga.up)
    assert t.head == tortuga.up

def test_right():
    t = tortuga.Turtle((500, 500))
    assert t.head == tortuga.right
    t.right()
    assert t.head == tortuga.down


def test_circle():
    t = tortuga.Turtle((500, 500))
    t.angle = math.pi / 18.
    for i in range(20):
        t.forward(10)
        if random.random() < 0.5:
            t.right()
        else:
            t.left()
    t.img.show()

def test_push_and_pop():
    t = tortuga.Turtle((500, 500))
    t.push()
    t.left()
    for i in range(100):
        t.forward()
    t.pop()
    for i in range(100):
        t.forward()
    t.img.show()

def test_grammar():
    t = tortuga.Turtle((500, 500))
    t.angle = 25.7 * math.pi / 180.0
    t.forward(50)
    t.push()
    t.right()
    t.forward(50)
    t.pop()
    t.forward(50)
    t.push()
    t.left()
    t.forward(50)
    t.pop()
    t.forward(50)
    t.img.show()


if __name__ == "__main__":
    pytest.main()
