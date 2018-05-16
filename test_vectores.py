#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi, cos, isclose
import pytest
from vectores import Vector2


def test_creacion():
    v = Vector2(3, 4)
    assert v.x == 3
    assert v.y == 4


def test_modulo():
    v = Vector2(3, 4)
    assert v.mod == 5


def test_modulo_2():
    v = Vector2(30, 40)
    assert v.mod == 50


def test_turn_left():
    v = Vector2(3, 4)
    v.turn_left() == Vector2(-4, 3)


def test_turn_right():
    v = Vector2(3, 4)
    v.turn_right() == Vector2(4, -3)


def test_addition():
    v1 = Vector2(3, 4)
    v2 = Vector2(5, 6)
    v = v1 + v2
    assert v.x == 8
    assert v.y == 10


def test_product_by_scalar():
    v = Vector2(3, 4) * 2
    assert v.x == 6
    assert v.y == 8


def test_product_by_vector():
    a = Vector2(3, 4)
    b = Vector2(5, 6)
    v = a @ b
    assert isclose(a.mod * b.mod * cos(a.theta - b.theta), v)

def test_perp_dot():
    assert Vector2(1, 0) @ Vector2(0, 1) == 0

def test_random():
    for _ in range(50):
        v = Vector2.random(800, 600)
        assert 0 <= v.x < 800
        assert 0 <= v.y < 600


def test_theta_zero_degrees():
    v = Vector2(1, 0)
    assert v.theta == 0


def test_theta_90_degrees():
    v = Vector2(0, 1)
    assert v.theta == pi / 2


def test_theta_180_degrees():
    v = Vector2(-1, 0)
    assert v.theta == pi


def test_set_theta():
    v = Vector2(1, 0)
    v.theta = pi/2
    assert v == Vector2(0, 1)


def test_theta_270_degrees():
    v = Vector2(0, -1)
    assert v.theta == - pi / 2

def test_as_tuple():
    v = Vector2(12, 56)
    assert v.as_tuple() == (12, 56)


if __name__ == "__main__":
    pytest.main()
