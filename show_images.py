#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pygame

image_extensiones = (
    '.jpg',
    '.jpeg',
    '.png',
    '.gif',
    )

def find_images(p='.'):
    result = []
    for (dirpath, dirnames, filenames) in os.walk(p):
        for filename in filenames:
            ext = os.path.splitext(filename)
            if ext in image_extensiones:
                full_name = os.path.join(dirpath, filename)
                result.append(full_name)
    return result





pygame.init()
