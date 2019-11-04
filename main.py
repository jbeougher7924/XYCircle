import pygame
import math


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


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
        pygame.draw.lines(screen, self.color, False, self.points, 1)
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
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    coords = 400, 200

    angle = 0
    rect = pygame.Rect(coords[0], coords[1], 20, 20)
    points = []
    points.append([int(coords[0]), int(coords[1])])
    speed = 1 # 30 is about 1 rev per 10 seconds
    next_tick = 1
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
    vert_circles.append(DrawCircle(RainBow[0], 30, test_coords, 90, 0.5, 1))
    test_coords = 100, 200
    vert_circles.append(DrawCircle(RainBow[1], 30, test_coords, 90, 0.5, 1))
    for i in range(7):
        pass

    # draw_test = DrawCircle(RED, 30, test_coords, 90, 0.5, 1)
    #
    # test_coords = 200, 100
    # draw_test_2 = DrawCircle(GREEN, 5, test_coords, 90, 0.5, 1)

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
        # draw_test.add_points(ticks)
        # draw_test_2.add_points(ticks)
        if ticks > next_tick:
            next_tick += speed
            angle += 1
            coords = move_coords(angle, 0.5, coords)
            rect.topleft = coords
            points.append([int(coords[0]), int (coords[1])])

        if points[-1] == [400, 199]:
            coords = 400, 200
            angle = 0
            temp = []
            temp.append(points[0])
            temp.append(points[1])
            points.clear()

            # points.append(temp[0])
            # points.append(temp[1])
            points.append([int(coords[0]), int(coords[1])])
            coords = move_coords(angle, 0.5, coords)
            points.append([int(coords[0]), int(coords[1])])
            # print("points[-1]")
            # print(points[-1])
            # print("coords")
            # print(coords)



        screen.fill((0, 0, 30))
        # screen.fill((0, 150, 150), rect)
        pygame.draw.lines(screen, BLUE, False, points, 2)
        pygame.draw.circle(screen, WHITE, [int(coords[0]), int(coords[1])], 4)
        for i in range(len(vert_circles)):
            vert_circles[i].draw_class(screen)
        # draw_test.draw_class(screen)
        # draw_test_2.draw_class(screen)
        pygame.display.flip()
        clock.tick(60)


    pygame.quit()


if __name__ == '__main__':
    main()