import pygame
import math


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)


RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (255, 0, 255)

class DrawSpline:
    def __init__(self, colorX, ColorY, speedX, speedY, coordsX, coordsY,  next_tick):
        self.color = colorX
        self.speed = (speedX + speedY) / 2
        self.coords = coordsX, coordsY
        self.rect = pygame.Rect(self.coords[0],self.coords[1], 20, 20)
        self.points = []
        self.next_tick = next_tick
        self.angle_init = self.angle
        self.coords_init = self.coords
        self.points.append([int(self.coords[0]), int(self.coords[1])])








class DrawCircle:
    def __init__(self, color, speed, coords, angle, radius, next_tick):
        self.color = color
        self.speed = speed
        self.coords = coords
        self.angle = angle
        self.radius = radius
        self.rect = pygame.Rect(self.coords[0],self.coords[1], 20, 20)
        self.points = []
        self.next_tick = next_tick
        self.angle_init = self.angle
        self.coords_init = self.coords
        self.points.append([int(coords[0]), int(coords[1])])

    def add_points(self, ticks):
        if ticks > self.next_tick:
            self.next_tick += self.speed
            self.angle += 1
            self.coords = move_coords(self.angle, self.radius, self.coords)
            self.rect.topleft = self.coords
            self.points.append([int(self.coords[0]), int (self.coords[1])])

        if self.points[-1] == [self.coords_init[0] -1, self.coords_init[1] -1]:
            self.coords = self.coords_init
            self.angle = self.angle_init
            self.points.clear()
            self.points.append([int(self.coords[0]), int (self.coords[1])])
            self.coords = move_coords(self.angle, self.radius, self.coords)
            self.points.append([int(self.coords[0]), int (self.coords[1])])

        # print("points[-1]")
        # print(self.points[-1])
        # print("coords")
        # print(self.coords)

    def draw_class(self, screen):
        # pygame.draw.lines(screen, self.color, False, self.points, 1)
        pygame.draw.circle(screen, self.color, [int(self.coords_init[0] - 30), int(self.coords_init[1])], 30, 1)
        pygame.draw.circle(screen, WHITE, [int(self.coords[0]), int(self.coords[1])], 4)


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
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()
    vert_circles = []
    RainBow = []
    RainBow.append(RED)
    RainBow.append(ORANGE)
    RainBow.append(YELLOW)
    RainBow.append(GREEN)
    RainBow.append(BLUE)
    RainBow.append(INDIGO)
    RainBow.append(VIOLET)
    test_coords = 100, 100

    for i in range(7):
        test_coords = 78, 110 + (78 * i)
        speed = 30 / (i + 1)
        vert_circles.append(DrawCircle(RainBow[i], speed, test_coords, 90, 0.5, 1))
        # test_coords = 150, 110 + (78 * i)
        # vert_circles.append(DrawCircle(RainBow[i], speed, test_coords, 90, 0.5, 1))

    for i in range(7):
        test_coords = 150 + (78 * i), 39
        speed = 30 / (i + 1)
        vert_circles.append(DrawCircle(RainBow[i], speed, test_coords, 90, 0.5, 1))

    # for i in range(7):
    #     for j in range(7):
    #         test_coords = 150 + (78 * i), 110 + (78 * j)
    #         speed = 30 / (i + 1)
    #         vert_circles.append(DrawCircle(RainBow[i], speed, test_coords, 90, 0.5, 1))




    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                running = False

        ticks = pygame.time.get_ticks()
        for i in range(len(vert_circles)):
            vert_circles[i].add_points(ticks)





        screen.fill((0, 0, 30))


        for i in range(len(vert_circles)):
            vert_circles[i].draw_class(screen)

        pygame.display.flip()
        clock.tick(360)


    pygame.quit()


if __name__ == '__main__':
    main()