import numpy as np
import matplotlib.pyplot as plt

N = 78
x = np.random.randint(1, 1000, N)
y = np.random.randint(1, 1000, N)
x_c = np.mean(x)
y_c = np.mean(y)
w = []


def draw(x, y, c, xz, yz, k):
    length = len(c)
    for i in range(0, length):
        color = (c[i] + 1) / k
        plt.scatter(x[i], y[i], color=(color, 0.2, color ** 2))
    plt.scatter(xz, yz, color='orange')
    plt.show()


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def check(x, y, xz, yz, clust, k):
    x_o, y_o = xz, yz
    clust(xz, yz, x, y, k, clust)
    a_clust(x, y, clust, k, xz, yz)
    draw(x, y, clust, xz, yz, k)

    if x_o == xz and y_o == yz:
        w = 0
        for i in range(0, k):
            sum = 0
            for j in range(0, len(clust)):
                if clust[j] == i:
                    sum += dist(x[j], y[j], xz[i], yz[i]) ** 2

            w += sum

        w.append(w)
        return True
    else:
        return False


def clust(xz, yz, x, y, k, cluster):
    for i in range(0, N):
        r = dist(xz[0], yz[0], x[i], y[i])
        f = 0
        for j in range(0, k):
            if r < dist(xz[j], yz[j], x[i], y[i]):
                f = j
                r = dist(xz[j], yz[j], x[i], y[i])
            if j == k - 1:
                cluster[i] = f


def a_clust(x, y, c, k, xz, yz):
    for i in range(0, k):
        z_x, z_y = [], []
        for j in range(0, len(c)):
            if c[j] == i:
                z_x.append(x[j])
                z_y.append(y[j])
        xz[i] = np.mean(z_x)
        yz[i] = np.mean(z_y)


def k_mean(k):
    q = 0
    for i in range(0, N):
        if dist(x_c, y_c, x[i], y[i]) > q:
            q = dist(x_c, y_c, x[i], y[i])
    xzz = [q * np.cos(2 * np.pi * i / k) + x_c for i in range(k)]
    yzz = [q * np.sin(2 * np.pi * i / k) + y_c for i in range(k)]
    cluster = [0] * N
    clust(xzz, yzz, x, y, k, cluster)
    draw(x, y, cluster, xzz, yzz, k)

    while not check(x, y, xzz, yzz, cluster, k):
        check(x, y, xzz, yzz, cluster, k)


if __name__ == "__main__":
    for i in range(1, 10):
        k_mean(i)
    plt.plot(range(1, 10), w)
    plt.xlabel('Cluster Num')
    plt.ylabel('WCSS')
    plt.show()
