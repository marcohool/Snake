import math

import pygame
import sys


class Square:
    global sqaureSize
    sqaureSize = 40

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect

    def draw(self):
        self.rect = self.x, self.y, sqaureSize, sqaureSize
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 0)


class Snake:
    def __init__(self, start_x, start_y):
        self.head = Square(start_x, start_y)
        self.body = []
        self.body.append(self.head)

    def draw(self):
        for i in self.body:
            Square.draw(i)


def drawScreen():
    screen.fill((0, 0, 0))
    Snake.draw(Snake(math.floor(screenWidth / 2 - (sqaureSize / 2)), math.floor(screenHeight / 2 - (sqaureSize / 2))))
    pygame.display.update()


def main():
    global screen, screenWidth, screenHeight

    screenWidth = 1280
    screenHeight = 720

    screen = pygame.display.set_mode((screenWidth, screenHeight))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.delay(50)
        clock.tick(10)
        drawScreen()


main()
