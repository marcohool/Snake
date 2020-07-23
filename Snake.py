import math
import pygame
import sys
import random

class Square:
    global squareSize

    squareSize = 40

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, squareSize, squareSize)

    def draw(self, color):
        pygame.draw.rect(screen, color, self.rect, 0)

    def moveHead(self, vector):
        self.rect.move_ip(round(vector.x), round(vector.y))
        if self.rect.y > screenHeight - squareSize:
            self.rect.y = 0
        if self.rect.x > screenWidth - squareSize:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = screenHeight
        if self.rect.x < 0:
            self.rect.x = screenWidth

    def getCoords(self):
        coords = pygame.Vector2()
        coords[:] = self.rect.x, self.rect.y
        return coords

    def setCoords(self, coords):
        self.rect.x = round(coords.x)
        self.rect.y = round(coords.y)


class Snake:
    def __init__(self, start_x, start_y):
        self.head = Square(start_x, start_y)
        self.body = []
        self.body.append(self.head)

    def draw(self):
        for i in self.body:
            Square.draw(i, (255, 0, 0))

    def getBody(self):
        return self.body

    def move(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.type == pygame.K_UP:
                    if moveCoords != (0, squareSize):
                        moveCoords[:] = 0, -squareSize
                        break
                elif event.key == pygame.K_s or event.type == pygame.K_DOWN:
                    if moveCoords != (0, -squareSize):
                        moveCoords[:] = 0, squareSize
                        break
                elif event.key == pygame.K_d or event.type == pygame.K_RIGHT:
                    if moveCoords != (-squareSize, 0):
                        moveCoords[:] = squareSize, 0
                        break
                elif event.key == pygame.K_a or event.type == pygame.K_LEFT:
                    if moveCoords != (squareSize, 0):
                        moveCoords[:] = -squareSize, 0
                        break

        if self.head.getCoords() == food.Square.getCoords():  # Food eaten
            food.respawnFood()
            self.body.append(Square(self.head.rect.x, self.head.rect.y))

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].rect.x = self.body[i - 1].rect.x
            self.body[i].rect.y = self.body[i - 1].rect.y

        self.head.moveHead(moveCoords)


class Food:
    def __init__(self, x, y):
        self.Square = Square(x, y)

    def drawFood(self):
        self.Square.draw((0, 255, 0))

    def respawnFood(self):
        coords = pygame.Vector2()
        coords[:] = random.randint(0, (screenWidth - squareSize) / squareSize) * squareSize, random.randint(0, (
                screenHeight - squareSize) / squareSize) * squareSize
        self.Square.setCoords(coords)


def collision():
    if len(snake.body) > 1:
        for i in range(1, len(snake.body)):
            if snake.head.getCoords() == snake.body[i].getCoords():
                return True

    return False


def drawScreen():
    screen.fill((0, 0, 0))
    snake.draw()
    food.drawFood()
    pygame.display.update()


def main():
    global screen, screenWidth, screenHeight, snake, moveCoords, food

    moveCoords = pygame.Vector2()

    screenWidth = 1280
    screenHeight = 720

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    snake = Snake(math.floor(screenWidth / 2 - squareSize), math.floor(screenHeight / 2 - squareSize))
    food = Food(random.randint(0, (screenWidth - squareSize) / squareSize) * squareSize,
                random.randint(0, (screenHeight - squareSize) / squareSize) * squareSize)

    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(59)
        clock.tick(60)
        Snake.move(snake)
        drawScreen()
        if collision():
            pygame.quit()
            sys.exit()

main()
