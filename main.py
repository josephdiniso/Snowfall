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
pygame.mixer.init(22050, -8, 16, 65536 )
pygame.display.set_caption("Snowfall")
size = (1000, 1000)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

class SnowBall:
    def __init__(self):
        self.x_orig = random.randint(0,size[0])
        self.x = self.x_orig
        self.y = -10
        self.y_velocity = random.randint(5,10)
        self.width = random.randint(100, 150)

    def forward(self):
        self.y += self.y_velocity
        self.x = self.x_orig + math.floor(self.width * math.sin(1.5*time.time()))


def main():
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
            if ball.y > size[1]:
                balls.remove(ball)
                del ball

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
        clock.tick(30)
        pygame.display.flip()


if __name__ == "__main__":
    main()