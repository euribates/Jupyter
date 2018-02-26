#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from PIL import Image

img = Image.open('./art/secret_shrek.png')
output = Image.new('RGB', img.size)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

for y in range(0, 500):
    for x in range(0, 500):
        pos = (x, y)
        r, g, blue = img.getpixel(pos)
        if blue % 2:
            output.putpixel(pos, BLACK)
        else:
            output.putpixel(pos, WHITE)

output.show()
