import matplotlib.pyplot as plt
import numpy as np

J = []
N = 1000
MIN = 1000000


def distention(z, p):
    return np.sqrt((z[0] - p[0]) ** 2 + (z[1] - p[1]) ** 2)


def nearest(points, c):
    cluster = np.zeros(len(points))
    for i in range(len(points)):
        min = np.infty
        for j in range(len(c)):
            if min > distention(points[i], c[j]):
                min = distention(points[i], c[j])
                cluster[i] = j
    return cluster


def plot(points, c, cluster):
    color_array = ['grey', 'orange', 'pink', 'm', 'k', 'purple', 'b', 'g', 'y', 'c']
    colors = []
    x = []
    y = []
    for i in range(len(points)):
        x.append(points[i][0])
        y.append(points[i][1])
        colors.append(color_array[int(cluster[i])])
    x_c = []
    y_c = []
    for i in range(len(c)):
        x_c.append(c[i][0])
        y_c.append(c[i][1])
    plt.scatter(x, y, color=colors)
    plt.scatter(x_c, y_c, color='r')
    plt.show()


def centroids(p, k):
    x = 0
    y = 0
    for i in range(len(p)):
        x = x + p[i][0]
        y = y + p[i][1]
    x = x / len(p)
    y = y / len(p)
    r = 0
    for i in range(len(p)):
        if r < distention([x, y], p[i]):
            r = distention([x, y], p[i])
    c = []
    for i in range(k):
        x_c = r * (np.cos(2 * np.pi * i / k)) + x
        y_c = r * (np.sin(2 * np.pi * i / k)) + y
        c.append([x_c, y_c])
    return c


def check(p, c, cluster, k):
    new_cluster = nearest(p, c)
    plot(p, c, cluster)
    count = 0
    for i in range(0, k):
        sum = 0
        for j in range(0, len(new_cluster)):
            if new_cluster[j] == i:
                sum = sum + distention(p[j], c[i]) ** 2
        count = count + sum
    J.append(count)
    return True


def kmeans(k, points):
    c = centroids(points, k)
    cluster = nearest(points, c)
    plot(points, c, cluster)
    while not check(points, c, cluster, k):
        check(points, c, cluster, k)


def koptimal_with_kmeans():
    points = []
    for i in range(N):
        points.append(np.random.randint(1, 100, 2))
    for i in range(1, 10):
        kmeans(i, points)
    global MIN
    array = []
    for i in range(1, len(J) - 1):
        array.append((J[i] - J[i + 1]) / (J[i - 1] - J[i]))
        if array[i - 1] < MIN:
            MIN = array[i - 1]
    print("k optimal:", array.index(MIN) + 2)


if __name__ == '__main__':
    koptimal_with_kmeans()
    plt.plot(range(1, 10), J)
    plt.xlabel('Cluster')
    plt.ylabel('J')
    plt.show()
