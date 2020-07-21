import math
import pygame
import sys


class Square:
    global squareSize

    squareSize = 40

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect

    def draw(self):
        self.rect = self.x, self.y, squareSize, squareSize
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 0)


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

            keys = pygame.key.get_pressed()

            for _ in keys:
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    pass
                elif keys[pygame.K_s or keys[pygame.K_DOWN]]:
                    pass
                elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    pass
                elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    pass

            snake.move()


def drawScreen():
    screen.fill((0, 0, 0))
    Snake.draw(snake)
    pygame.display.update()


def main():
    global screen, screenWidth, screenHeight, snake

    screenWidth = 1280
    screenHeight = 720

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    snake = Snake(math.floor(screenWidth / 2 - (squareSize / 2)), math.floor(screenHeight / 2 - (squareSize / 2)))

    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(50)
        clock.tick(10)
        Snake.move(snake)
        drawScreen()


main()
