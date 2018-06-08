version = '5.0'

import math
import pygame
import random
import time

from pygame.locals import Rect
from math import pi
import vectores
from vectores import Vector2

SIZE = WIDTH, HEIGHT = 800, 600  # Tamaño de pantalla
CENTER = (WIDTH//2, HEIGHT//2)

BLACK = (0, 0, 0)                # Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

FPS = 30                         # Velocidad del juego


def draw_vector(screen, color, vector, origin=(0, 0)):
    origin = Vector2(origin)
    pygame.draw.line(screen, color, origin, origin+vector)
    pygame.draw.circle(screen, color, origin, 3)
    arrow_point = origin + vector
    orientation = vector.unit() * 10
    orientation.theta -= 7*pi/8
    left_wing =  arrow_point + orientation 
    orientation.theta -= pi/4
    right_wing =  arrow_point + orientation
    pygame.draw.polygon(screen, color, [arrow_point, left_wing, right_wing])
    

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, x=0, y=0):
        super().__init__() 
        self.frames = [
            pygame.image.load('pong/ball_00.png'),
            pygame.image.load('pong/ball_01.png'),
            pygame.image.load('pong/ball_02.png'),
        ]
        self.num_frames = len(self.frames)
        self.counter = 0
        self.image = self.frames[self.counter]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10
        self.reset()

    def reset(self):
        self.rect.center = CENTER
        self.speed = 10
        if random.random() < 0.5:
            self.orientation = Vector2.Right()
        else:
            self.orientation = Vector2.Left()
        # self.orientation.theta += random.uniform(pi/4, -pi/4)
        
    def bounce(self):
        self.orientation.theta = -self.orientation.theta

    def update(self):
        delta = self.orientation * self.speed
        self.rect.center = Vector2(self.rect.center) + delta
        hit_walls = False
        if self.rect.top < 0:
            self.rect.top = 0
            self.bounce()
            hit_walls = True
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.bounce()
            hit_walls = True
        self.counter = self.counter + 1
        self.image = self.frames[self.counter% self.num_frames]
        if self.counter % FPS == 0:
            self.speed += .25
        return hit_walls


class InputState:
    
    def __init__(self):
        self.left_up = False
        self.left_down = False
        self.right_up = False
        self.right_down = False
        self.exit = False
        
    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.exit = True
                elif event.key == pygame.K_w:
                    self.left_up = True
                elif event.key == pygame.K_s:
                    self.left_down = True
                elif event.key == pygame.K_UP:
                    self.right_up = True
                elif event.key == pygame.K_DOWN:
                    self.right_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.left_up = False
                elif event.key == pygame.K_s:
                    self.left_down = False
                elif event.key == pygame.K_UP:
                    self.right_up = False
                elif event.key == pygame.K_DOWN:
                    self.right_down = False


class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.frames = [
            pygame.image.load('pong/paddle_00.png'),
            pygame.image.load('pong/paddle_01.png'),
            pygame.image.load('pong/paddle_02.png'),
        ]
        self.num_frames = len(self.frames)
        self.counter = 0
        self.image = self.frames[self.counter]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect = self.rect.move(0, self.speed)
        self.counter = (self.counter + 1) % self.num_frames
        self.image = self.frames[self.counter]
        
    def go_up(self):
        self.speed = -10

    def go_down(self):
        self.speed = 10
        
    def stop(self):
        self.speed = 0

        
class LeftPad(Paddle):
    
    def update(self, inputs):
        if inputs.left_up:
            self.go_up()
        elif inputs.left_down:
            self.go_down()
        else:  
            self.stop()
        super().update()
        
class RightPad(Paddle):
    
    def update(self, inputs):
        if inputs.right_up:
            self.go_up()
        elif inputs.right_down:
            self.go_down()
        else:
            self.stop()        
        super().update()   


class Game:
    
    def __init__(self, screen):
        self.screen = screen
        box = self.screen.get_rect()
        self.width, self.height = box.width, box.height
        self.center = Vector2(self.width // 2, self.height // 2)
        self.r_paddle = RightPad(self.width - 50, self.center.y)
        self.l_paddle = LeftPad(50, self.center.y)
        self.ball = Ball(self.center.x, self.center.y)
        self.all_objects = pygame.sprite.Group(
            self.ball, 
            self.r_paddle,
            self.l_paddle
            )
        self.score = {
            'left': 0,
            'right': 0,
            }
        self.load_resources()
        self.reset()

    def load_resources(self):
        self.background = pygame.image.load('pong/background.png')
        self.font = pygame.font.Font('pong/fonts/arcade.ttf', 90)
        self.paddle_sound = pygame.mixer.Sound('pong/audio/ping_paddle.wav')
        self.plop_sound = pygame.mixer.Sound('pong/audio/pong_plop.wav')

    def reset(self):
        self.counter = 3 * FPS
        self.ball.reset()
    
    def calc_bounce_angle(self, pos):
        pos = Vector2(pos)
        ball_pos = Vector2(self.ball.rect.center)
        delta = pos.y - ball_pos.y
        delta = min(delta, 55) if delta > 0 else max(delta, -55)
        if ball_pos.x < pos.x:  # Bounces on right paddle
            result = Vector2.Left()
            result.theta = pi + delta * pi / 200
        else:
            result = Vector2.Right()
            result.theta = -delta * pi / 200
        return result
    
    def update(self, inputs):
        self.r_paddle.update(inputs)
        self.l_paddle.update(inputs)
        hit_walls = self.ball.update() 
        if hit_walls:
            print('hit walls')
            self.plop_sound.play()
        hit_paddle = False
        if self.ball.rect.colliderect(self.l_paddle.rect):
            print('ball hists left paddle')
            self.ball.rect.left = self.l_paddle.rect.right
            self.ball.orientation = self.calc_bounce_angle(self.l_paddle.rect.center)
            hit_paddle = True
        elif self.ball.rect.colliderect(self.r_paddle.rect):
            print('ball hists right paddle',time.time())
            self.ball.rect.right = self.r_paddle.rect.left
            self.ball.orientation = self.calc_bounce_angle(self.r_paddle.rect.center)
            hit_paddle = True
        if hit_paddle:
            self.paddle_sound.play()
        
    def left_wins(self):
        return self.ball.rect.left < 0

    def right_wins(self):
         return self.ball.rect.right > WIDTH

    def draw(self, trace_on=False):
        self.screen.blit(self.background, (0, 0))
        self.draw_score()
        if self.counter > 0:
            seconds = self.counter // FPS
        self.all_objects.draw(screen)
        if trace_on:
            for item in self.all_objects.sprites():
                pygame.draw.rect(screen, RED, item.rect, 1)
            draw_vector(self.screen, CYAN, self.ball.orientation*25, self.ball.rect.center)
            for pad in (self.l_paddle, self.r_paddle):
                origin = Vector2(pad.rect.center)
                expected_bounce = self.calc_bounce_angle(origin)
                draw_vector(self.screen, YELLOW, expected_bounce*100, origin)
        pygame.display.update()

    def draw_text(self, text, position):
        img = self.font.render(str(text), True, GREEN)
        rect = img.get_rect()
        rect.center = position
        self.screen.blit(img, rect)
        
    def draw_score(self):
        self.draw_text(self.score['left'], (200, 50))
        self.draw_text(self.score['right'], (600, 50))

    
pygame.init()
try:
    pygame.display.set_caption(version)
    screen = pygame.display.set_mode(SIZE, 0, 24)
    game = Game(screen)
    clock = pygame.time.Clock()    
    input_state = InputState()
    
    while True:
        input_state.check()
        if input_state.exit:
            break
        game.update(input_state)
        if game.left_wins():
            game.score['left'] += 1
            game.reset()
        if game.right_wins():
            game.score['right'] += 1
            game.reset()
        game.draw(trace_on=True)
        clock.tick(FPS)
        if game.score['left'] > 15 or game.score['right'] > 15:
            break
finally:
    pygame.quit()
