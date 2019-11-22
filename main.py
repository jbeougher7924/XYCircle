import pygame
import math

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

RED = [255, 0, 0]
ORANGE = [255, 128, 0]
YELLOW = [255, 255, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
INDIGO = [75, 0, 130]
VIOLET = [255, 0, 255]


class DrawSpline:
    shared_coords = {}

    def __init__(self, colorX, colorY, speedX, speedY, coordsX, coordsY, indexX, indexY, next_tick):
        self.color = [(colorX[0] + colorY[0]) / 2, (colorX[1] + colorY[1]) / 2, (colorX[2] + colorY[2]) / 2]
        self.speed = (speedX + speedY) / 2
        self.coords = coordsX, coordsY
        self.rect = pygame.Rect(self.coords[0], self.coords[1], 20, 20)
        self.points = []
        self.next_tick = next_tick
        self.coords_init = self.coords
        self.indexX = indexX
        self.indexY = indexY
        self.points.append([int(self.coords[0]), int(self.coords[1])])

    def add_points(self, ticks, reset):

        # print("X: {} Y: {}".format(self.indexX, self.indexY))

        if ticks > self.next_tick:
            self.next_tick += self.speed

            xCoords = self.shared_coords[self.indexX]
            yCoords = self.shared_coords[self.indexY + 7]

            # print(xCoords)
            # print(yCoords)
            # print("*******")

            # self.coords = (xCoords[0] - self.coords_init[0] + ((145 * (self.indexX + 2) ) )) - (67  - (11 * self.indexX )) , yCoords[1]
            self.coords = yCoords[0], xCoords[1]

            if self.indexX == 1:
                pass
            # print("self.coords '{}' = xCoords[0] '{}' - self.coords_init[0] '{}' + (145 + (78 * (self.indexY '{}' + 1))), yCoords[1] '{}' ".format(self.coords, xCoords[0], self.coords_init[0], self.indexY, yCoords[1]))
                # self.coords = self.coords[0] + 10, self.coords[1]

            # print("X: {} Y: {}".format(self.coords_init[0], self.coords_init[1]))
            # print("X: {} Y: {}".format(xCoords[0], yCoords[1]))
            # print(self.coords)
            # self.coords = xCoords, yCoords
            # self.angle = 90
            # self.radius = 0.5
            # move_coords(self.angle, self.radius, self.coords)
            self.rect.topleft = self.coords
            self.points.append([int(self.coords[0]), int(self.coords[1])])
            # print(self.points)


        if reset:
            self.coords = self.coords_init
            temp = []
            temp.append(self.points[1])
            self.points.clear()
            self.points.append([int(self.coords[0]), int(self.coords[1])])
            self.points.append(temp[0])

    def add_points_2(self, ticks, reset):

        # print("X: {} Y: {}".format(self.indexX, self.indexY))

        if ticks > self.next_tick:
            self.next_tick += self.speed


            xCoords = self.shared_coords[self.indexX]
            yCoords = self.shared_coords[self.indexY]
            # self.coords =  xCoords[0] - self.coords_init[0] + (150 + (78 * (self.indexY + 1 ))) , yCoords[1]
            self.coords = (xCoords[0] - self.coords_init[0] + ((145 * (self.indexX + 2) ) )) - (67  - (11 * self.indexX )) , yCoords[1]

            if self.indexX == 1:
                pass
            # print("self.coords '{}' = xCoords[0] '{}' - self.coords_init[0] '{}' + (145 + (78 * (self.indexY '{}' + 1))), yCoords[1] '{}' ".format(self.coords, xCoords[0], self.coords_init[0], self.indexY, yCoords[1]))
                # self.coords = self.coords[0] + 10, self.coords[1]

            # print("X: {} Y: {}".format(self.coords_init[0], self.coords_init[1]))
            # print("X: {} Y: {}".format(xCoords[0], yCoords[1]))
            # print(self.coords)
            # self.coords = xCoords, yCoords
            # self.angle = 90
            # self.radius = 0.5
            # move_coords(self.angle, self.radius, self.coords)
            self.rect.topleft = self.coords
            self.points.append([int(self.coords[0]), int(self.coords[1])])


        if reset:
            self.coords = self.coords_init
            temp = []
            temp.append(self.points[1])
            self.points.clear()
            self.points.append([int(self.coords[0]), int(self.coords[1])])
            self.points.append(temp[0])

    def draw_class(self, screen):
        pygame.draw.line(screen, self.color, self.points[-2], self.points[-1], 1)
        # pygame.draw.circle(screen, self.color, [int(self.coords_init[0] - 30), int(self.coords_init[1])], 30, 1)

    def put_shared_coords(self, shared_coords):
        self.shared_coords = shared_coords


class DrawCircle:
    shared_coords = {}

    def __init__(self, color, speed, coords, angle, radius, next_tick, index):

        self.color = color
        self.speed = speed
        self.coords = coords
        self.angle = angle
        self.radius = radius
        self.rect = pygame.Rect(self.coords[0], self.coords[1], 20, 20)
        self.points = []
        self.next_tick = next_tick
        self.angle_init = self.angle
        self.coords_init = self.coords
        self.points.append([int(coords[0]), int(coords[1])])
        self.index = index
        self.shared_coords[self.index] = self.coords

    def add_points(self, ticks):
        # if self.index == 7:
        #     print(self.coords)
        if ticks > self.next_tick:
            self.next_tick += self.speed
            self.angle += 1
            self.coords = move_coords(self.angle, self.radius, self.coords)
            self.rect.topleft = self.coords

            self.shared_coords[self.index] = self.coords

        # if self.points[-1] == [self.coords_init[0] - 1, self.coords_init[1] - 1]:
        #     self.coords = self.coords_init
        #     self.angle = self.angle_init
        #     self.points.clear()
        #     self.points.append([int(self.coords[0]), int(self.coords[1])])
        #     self.coords = move_coords(self.angle, self.radius, self.coords)
        #     self.points.append([int(self.coords[0]), int(self.coords[1])])
        #     if self.index == 0:
        #         return True

        if self.angle == 90 + 360:
            self.coords = self.coords_init
            self.angle = self.angle_init

            if self.index == 0:
                return True

        return False

    def draw_class(self, screen):
        # pygame.draw.lines(screen, self.color, False, self.points, 1)
        pygame.draw.circle(screen, self.color, [int(self.coords_init[0] - 30), int(self.coords_init[1])], 30, 1)
        pygame.draw.circle(screen, WHITE, [int(self.coords[0]), int(self.coords[1])], 4)

    def get_shared_coords(self):
        return self.shared_coords


def move_coords(angle, radius, coords):
    theta = math.radians(angle)
    return coords[0] + radius * math.cos(theta), coords[1] + radius * math.sin(theta)


def drawHouse(x, y, width, height, screen, color):
    points = [(x, y - ((2 / 3.0) * height)), (x, y), (x + width, y), (x + width, y - (2 / 3.0) * height),
              (x, y - ((2 / 3.0) * height)), (x + width / 2.0, y - height), (x + width, y - (2 / 3.0) * height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)


def main():
    pygame.display.set_caption("Oribit")
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()
    vert_circles = []
    splines = []
    RainBow = []
    RainBow.append(RED)
    RainBow.append(ORANGE)
    RainBow.append(YELLOW)
    RainBow.append(GREEN)
    RainBow.append(BLUE)
    RainBow.append(INDIGO)
    RainBow.append(VIOLET)

    for i in range(7):
        test_coords = 78, 110 + (78 * i)
        speed = 30 / (i + 1)
        vert_circles.append(DrawCircle(RainBow[i], speed, test_coords, 90, 0.5, 1, i))
        # test_coords = 150, 110 + (78 * i)
        # vert_circles.append(DrawCircle(RainBow[i], speed, test_coords, 90, 0.5, 1))

    for i in range(7):
        test_coords = 150 + (78 * i), 39
        speed = 30 / (i + 1)
        vert_circles.append(DrawCircle(RainBow[i], speed, test_coords, 90, 0.5, 1, i + 7))

        for x in range(7):
            xCoords = 150 + (78 * x) - 40
            for y in range(7):
                speedX = 30 / (x + 1)
                speedY = 30 / (y + 1)
                yCoords = 110 + (78 * y) + 39
                splines.append(DrawSpline(RainBow[x], RainBow[y], speedX, speedY, yCoords, xCoords, x, y, 1))



    running = True
    reset = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                running = False

        ticks = pygame.time.get_ticks()

        for vert_circle in vert_circles:
            reset.append( vert_circle.add_points(ticks))

        for spline in splines:
            spline.put_shared_coords(vert_circles[0].get_shared_coords())
            spline.add_points(ticks, reset[0])

        # test_coords =  78, 110 + (78 * i)
        # pygame.Rect(self.coords[0], self.coords[1], 20, 20)

        vert_fill = pygame.Rect(84, 6, 540, 65)
        screen.fill(BLACK, vert_fill)

        # test_coords = 150 + (78 * i), 39
        hortz_fill = pygame.Rect(15, 75, 67, 535)
        screen.fill(BLACK, hortz_fill)

        if(reset[0]):
            spline_fill = pygame.Rect(78, 72, 545, 545)
            screen.fill(BLACK, spline_fill)

        for vert_circle in vert_circles:
            vert_circle.draw_class(screen)

        for spline in splines:
            spline.draw_class(screen)

        reset.clear()
        pygame.display.flip()
        clock.tick(360)

    pygame.quit()


if __name__ == '__main__':
    main()
