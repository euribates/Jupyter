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

NUM_FRAMES = 100
for frame in range(NUM_FRAMES):
    print('Generando frame {}'.format(frame), end=' ')
    output = Image.new('RGB', size)
    for y in range(0, height):
        frontera_x = int(round(frame * width / NUM_FRAMES))
        for x in range(0, width):
            pos = (x, y)
            color_from = img_from.getpixel(pos)
            color_to = img_to.getpixel(pos)
            if x < frontera_x:
                output.putpixel(pos, color_from)
            else:
                output.putpixel(pos, color_to)
    output.save('movie/frame_{:04d}.png'.format(frame), 'PNG')
    print('[OK]')
