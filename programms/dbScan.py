import pygame
import numpy as np

colors = ["#ffe4e1", "#eac93c", "#0d324d", "#637dac", "#242533", "#724ea2", "#b6e2ad", "#bce9f1", "#a981a9"]


def dist(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def neighbours(point1, points, groups, flags, e, g):
    for i, pnt2 in enumerate(points):
        if groups[i] == 0 and dist(point1, pnt2) < e:
            groups[i] = g
            if flags[i] != 'y':
                neighbours(pnt2, points, groups, flags, e, g)


def dbscan(points):
    min_points = 3
    eps = 60

    f = ['r' for _ in range(len(points))]

    for i, point1 in enumerate(points):
        number_of_points = 0

        for point2 in points:
            if point1 != point2 and dist(point1, point2) < eps:
                number_of_points += 1

        if number_of_points >= min_points:
            f[i] = 'g'

    for i, point1 in enumerate(points):
        if f[i] != 'g':
            for j, point2 in enumerate(points):
                if f[j] == 'g' and point1 != point2 and dist(point1, point2) < eps:
                    f[i] = 'y'
                    break

    groups = [0 for _ in range(len(points))]

    g = 0
    for i, point1 in enumerate(points):
        if f[i] == 'g' and groups[i] == 0:
            g += 1
            neighbours(point1, points, groups, f, eps, g)

    return f, groups


def start():
    pygame.init()

    s = pygame.display.set_mode((800, 600))
    running = True

    s.fill("white")

    pygame.display.update()
    points = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    points.append(event.p)
                    pygame.draw.circle(s, color='black', center=event.p, radius=10)
                    pygame.display.update()
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_1:
                    flags, groups = dbscan(points)
                    s.fill("white")
                    for i, pnt in enumerate(points):
                        clr = flags[i]
                        if clr == 'r':
                            clr = 'red'
                        elif clr == 'y':
                            clr = 'yellow'
                        else:
                            clr = 'green'
                        pygame.draw.circle(s, color=clr, center=pnt, radius=10)
                    pygame.display.update()
                if event.key == pygame.K_2:
                    flags, groups = dbscan(points)
                    s.fill('white')
                    for i, pnt in enumerate(points):
                        pygame.draw.circle(s, color=colors[groups[i]], center=pnt, radius=10)
                    pygame.display.update()
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    start()
