#!/usr/src/env python3
import random
import time
import math

import pygame

size = (600,600)
BLACK = (0,0,0)
WHITE = (255,255,255)

# PyGame inits
pygame.init()
pygame.display.set_caption("Snowfall")
size = (1000, 1000)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

class SnowBall:
    def __init__(self):
        self.x_orig = random.randint(0,screen.get_width())
        self.x = self.x_orig
        self.y = -10
        self.y_velocity = random.randint(5,10)
        self.width = random.randint(100, 150)

    def forward(self):
        self.y += self.y_velocity
        self.x = self.x_orig + math.floor(self.width * math.sin(1.5*time.time()))


def main():
    global screen
    done = False
    balls = []
    while not done:
        screen.fill(BLACK)
        while len(balls) < 150:
            ball = SnowBall()
            balls.append(ball)
        for ball in balls:
            ball.forward()
            pygame.draw.circle(screen, WHITE, (ball.x, ball.y), 4)
            if ball.y > screen.get_height():
                balls.remove(ball)
                del ball
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.K_DOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_Q)):
                pygame.quit()
                done = True
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
        clock.tick(30)
        pygame.display.flip()


if __name__ == "__main__":
    main()