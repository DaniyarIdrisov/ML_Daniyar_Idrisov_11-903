import numpy as np
import pygame
from sklearn import svm
from sklearn.datasets import make_blobs

running = True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 0)
YELLOW = (0, 255, 0)
BROWN = (0, 0, 255)


def start():
    global running
    # Создаётся 2 кучки, с 40 точками, и центрами в (100, 100), (700, 500) и стандартным отклонием 50
    points, labels = make_blobs(n_samples=40, centers=2, center_box=((100, 100), (700, 500)), cluster_std=50)
    # C Параметр регуляризации. Сила регуляризации обратно пропорциональна C.
    # Должна быть строго положительной. Штраф представляет собой штраф в квадрате l2.
    clf = svm.SVC(kernel='linear', C=1000)
    clf.fit(points, labels)
    # фиолетовое 0, иначе черное
    colors = [PURPLE if label == 0 else BLACK for label in labels]
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    screen.fill(WHITE)
    pygame.display.set_caption("SVM")
    d = []
    dc = []
    x = np.linspace(0, 800)
    #веса
    w = clf.coef_[0]
    # вычислим коэффициент наклона перед x
    a = -w[0] / w[1]
    # уравнение прямой, со сдвигом (clf.intercept_[0]) / w[1]
    y = a * x - (clf.intercept_[0]) / w[1]
    print('yy', y)
    while running:
        mouse = pygame.mouse.get_pos()
        for point in zip(x, y):
            pygame.draw.circle(screen, BROWN, point, 1)
        for point in zip(points, colors):
            pygame.draw.circle(screen, point[1], point[0], 5)
        for point in zip(d, dc):
            pygame.draw.circle(screen, point[1], point[0], 5)
        for point in clf.support_vectors_:
            center = int(point[0]), int(point[1])
            pygame.draw.circle(screen, YELLOW, center, 10, 2)
        pygame.draw.line(screen, BROWN, (x[0], y[0]), (x[-1], y[-1]), 1)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                predicted_class = clf.predict([mouse])
                d.append(mouse)
                if predicted_class == 0:
                    color = PURPLE
                else:
                    color = BLACK
                dc.append(color)
            if event.type == pygame.QUIT:
                running = False
                print('THE END')
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    print("START GAME")
    start()
