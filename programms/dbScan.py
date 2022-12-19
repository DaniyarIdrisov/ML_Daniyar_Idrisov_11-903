import pygame
import numpy as np

MIN = 6
EPS = 60
COLORS = ["#f08077", "#bce9f1", "#5a3036", "#637dac", "#eac93c", "#b6e2ad", "#5c8910", "#724ea2"]


def neighbors(p1, points, groups, f, g):
    for i, p2 in enumerate(points):
        if groups[i] == 0 and dist(p1, p2) < EPS:
            groups[i] = g
            if f[i] != 'y':
                neighbors(p2, points, groups, f, g)


def dist(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def dbscan(points):
    f = ['r' for _ in range(len(points))]
    for i, p1 in enumerate(points):
        n = 0
        for p2 in points:
            if p1 != p2 and dist(p1, p2) < EPS:
                n += 1
        if n >= MIN:
            f[i] = 'g'
    for i, p1 in enumerate(points):
        if f[i] != 'g':
            for j, p2 in enumerate(points):
                if f[j] == 'g' and p1 != p2 and dist(p1, p2) < EPS:
                    f[i] = 'y'
                    break
    groups = [0 for _ in range(len(points))]
    g = 0
    for i, p1 in enumerate(points):
        if f[i] == 'g' and groups[i] == 0:
            g += 1
            neighbors(p1, points, groups, f, g)
    return f, groups


if __name__ == 'main':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True
    screen.fill("white")
    pygame.display.update()
    p = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    p.append(event.pos)
                    pygame.draw.circle(screen, color='black', center=event.pos, radius=10)
                    pygame.display.update()
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_1:
                    flags, groups = dbscan(p)
                    screen.fill("white")
                    for i, pnt in enumerate(p):
                        color = flags[i]
                        if color == 'r':
                            color = 'red'
                        elif color == 'y':
                            color = 'yellow'
                        else:
                            color = 'green'
                        pygame.draw.circle(screen, color=color, center=pnt, radius=10)
                    pygame.display.update()
                if event.key == pygame.K_2:
                    flags, groups = dbscan(p)
                    screen.fill('white')
                    for i, pnt in enumerate(p):
                        pygame.draw.circle(screen, color=COLORS[groups[i]], center=pnt, radius=10)
                    pygame.display.update()
            if event.type == pygame.QUIT:
                running = False
