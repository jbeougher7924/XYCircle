import pygame
import math


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


class DrawCircle:
    def __init__(self, color, speed, coords, angle, rect, points, next_tick):
        self.color = color
        self.speed = speed
        self.coords = coords
        self.angle = angle
        self.rect = rect
        self.points = points
        self.next_tick = next_tickM


def move_coords(angle, radius, coords):
    theta = math.radians(angle)
    return coords[0] + radius * math.cos(theta), coords[1] + radius * math.sin(theta)

def drawHouse(x, y, width, height, screen, color):
    points = [(x,y- ((2/3.0) * height)), (x,y), (x+width,y), (x+width,y-(2/3.0) * height),
        (x,y- ((2/3.0) * height)), (x + width/2.0,y-height), (x+width,y-(2/3.0)*height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)

def main():
    pygame.display.set_caption("Oribit")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    coords = 400, 200

    angle = 0
    rect = pygame.Rect(*coords, 20, 20)
    points = []
    points.append([int(coords[0]), int(coords[1])])
    speed = 1
    next_tick = 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                running = False

        ticks = pygame.time.get_ticks()

        if ticks > next_tick:
            next_tick += speed
            angle += 1
            coords = move_coords(angle, 2, coords)
            rect.topleft = coords
            points.append([int(coords[0]), int (coords[1])])

        if points[-1] == [400, 199]:
            coords = 400, 200
            angle = 0
            temp = []
            temp.append(points[0])
            temp.append(points[1])
            points.clear()
            points.append(temp[0])
            points.append(temp[1])

            print(points[-1])
            print(coords)



        screen.fill((0, 0, 30))
        # screen.fill((0, 150, 150), rect)
        pygame.draw.circle(screen, WHITE, [int(coords[0]), int (coords[1])], 4)
        pygame.draw.lines(screen, BLUE, False, points, 4)
        pygame.display.flip()
        clock.tick(150)


    pygame.quit()


if __name__ == '__main__':
    main()