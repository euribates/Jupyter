#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import math
from PIL import Image

def ramp(from_val, to_val, percent):
    f = percent / 100.0
    return int(round(from_val * (1 - f) + to_val * f))


img_from = Image.open('./art/clark-kent.png')
img_to = Image.open('./art/superman.png')

assert img_from.size == img_to.size
width, height = size = img_from.size

for frame in range(0, 100):
    print('Generando frame {}'.format(frame), end=' ')
    output = Image.new('RGB', size)
    for y in range(0, height):
        for x in range(0, width):
            pos = (x, y)
            color_from = img_from.getpixel(pos)
            color_to = img_to.getpixel(pos)
            percent = frame * 1
            red = ramp(color_from[0], color_to[0], percent)
            green = ramp(color_from[1], color_to[1], percent)
            blue = ramp(color_from[2], color_to[2], percent)
            output.putpixel(pos, (red, green, blue))
    output.save('movie/frame_{:04d}.png'.format(frame), 'PNG')
    print('[OK]')
