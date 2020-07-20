import pygame
import sys


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, 25, 25)
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
    Snake.draw(Snake(20, 20))
    pygame.display.update()




def main():
    global screen

    screen_width = 1280
    screen_height = 720

    screen = pygame.display.set_mode((screen_width, screen_height))

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
