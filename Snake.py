import math
import pygame
import sys


class Square:
    global squareSize

    squareSize = 40

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, squareSize, squareSize)

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 0)

    def move(self, vector):
        self.rect.move_ip(vector.x, vector.y)


class Snake:
    def __init__(self, start_x, start_y):
        self.head = Square(start_x, start_y)
        self.body = []
        self.body.append(self.head)

    def draw(self):
        for i in self.body:
            Square.draw(i)

    def move(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.type == pygame.K_UP:
                    if move != (0, squareSize):
                        move[:] = 0, -squareSize
                elif event.key == pygame.K_s or event.type == pygame.K_DOWN:
                    if move != (0, -squareSize):
                        move[:] = 0, squareSize
                elif event.key == pygame.K_d or event.type == pygame.K_RIGHT:
                    if move != (-squareSize, 0):
                        move[:] = squareSize, 0
                elif event.key == pygame.K_a or event.type == pygame.K_LEFT:
                    if move != (squareSize, 0):
                        move[:] = -squareSize, 0

        self.head.move(move)


def drawScreen():
    screen.fill((0, 0, 0))
    Snake.draw(snake)
    pygame.display.update()


def main():
    global screen, screenWidth, screenHeight, snake, move

    move = pygame.Vector2()

    screenWidth = 1280
    screenHeight = 720

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    snake = Snake(math.floor(screenWidth / 2 - (squareSize / 2)), math.floor(screenHeight / 2 - (squareSize / 2)))

    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(90)
        clock.tick(60)
        Snake.move(snake)
        drawScreen()


main()
