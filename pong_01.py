#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import pygame

FPS = 60
SIZE = WIDTH, HEIGHT = (800, 600)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Ball:

    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

    def update(self):
        pass

    def draw(self, src):
        rect = pygame.Rect(self.x-5, self.y-5, 10, 10)
        pygame.draw.rect(src, WHITE, rect) 


def main():
    try:
        pygame.init()
        pygame.display.set_caption("Pong 0.1")
        screen = pygame.display.set_mode(SIZE, 0, 24)

        # Inicialización del juego
        clock = pygame.time.Clock()    
        ball = Ball()
        in_game = True  # Indicador lógico para saber cuando debemos terminar el juego

        while in_game:

            # Obtener datos de entrada
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_game = False
            
            # Recalcular el estado del juego, en base al estado actual y a las entradas
            ball.update()
            
            # Representamos el nuevo estado
            screen.fill(BLACK)
            ball.draw(screen)
            pygame.display.update()
            clock.tick(FPS)
    finally:
        pygame.quit()

if __name__ == '__main__':
    main()
