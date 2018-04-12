#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from PIL import Image

img = Image.open('./art/shrek.png')
mask = Image.open('./art/hola.png')

for y in range(0, 500):
    for x in range(0, 500):
        pos = (x, y)
        bit = mask.getpixel(pos)
        r, g, blue = img.getpixel(pos)
        if blue % 2 != bit:
            blue += 1 if blue < 128 else -1
            img.putpixel((x, y), (r, g, blue))

img.save('./art/secret_shrek.png')
