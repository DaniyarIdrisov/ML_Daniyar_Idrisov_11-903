import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def draw(matrix, matrix_main, n):
    result = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != -1:
                result[i][j] = matrix[i][j] * matrix_main[i][j]
            else:
                result[i][j] = -1
    g = nx.Graph(result)
    p = nx.spring_layout(g)
    e = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, p, e)
    nx.draw(g, p)
    plt.show()


def divide(matrix_min):
    maxim = 0
    maxI, maxJ = -1, -1
    for i in range(n):
        for j in range(i + 1, n):
            if matrix_min[i][j] == 1:
                if begin_matrix[i][j] > maxim:
                    maxim = begin_matrix[i][j]
                    maxI, maxJ = i, j
    matrix_min[maxI][maxJ] = 0
    matrix_min[maxJ][maxI] = 0
    return matrix_min


def alg(matrix, n, k):
    matrix_min = np.zeros((n, n))
    matrix_min = begin(matrix_min)
    for i in range(n - 2):
        matrix_min = mo(matrix_min)
    r = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if matrix_min[i][j] != -1:
                r[i][j] = matrix_min[i][j] * begin_matrix[i][j]
            else:
                r[i][j] = -1

    g = nx.Graph(r)
    p = nx.spring_layout(g)
    e = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, p, e)
    nx.draw(g, p)
    plt.show()
    for i in range(k - 1):
        matrix_min = divide(matrix_min)

    draw(matrix_min, matrix, n)


def begin(matrix):
    min = begin_matrix[0][1]
    minI, minJ = 0, 1
    for i in range(n):
        for j in range(i + 1, n):
            if min > begin_matrix[i][j] and begin_matrix[i][j] != 0:
                min = begin_matrix[i][j]
                minI, minJ = i, j
    matrix[minI][minJ] = matrix[minJ][minI] = 1
    matrix[minI][minI] = matrix[minJ][minJ] = -1
    return matrix


def mo(matrix_min):
    minim = None
    minI, minJ = 0, 1
    for i in range(n):
        if matrix_min[i][i] == -1:
            for j in range(n):
                if matrix_min[j][j] == 0:
                    if minim is None or (minim > begin_matrix[i][j] and begin_matrix[i][j] != 0):
                        minim = begin_matrix[i][j]
                        minI, minJ = i, j
    matrix_min[minI][minJ] = matrix_min[minJ][minI] = 1
    matrix_min[minI][minI] = matrix_min[minJ][minJ] = -1
    return matrix_min


if __name__ == '__main__':
    n, k = 5, 2
    begin_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            if i == 3:
                begin_matrix[i][j] = begin_matrix[j][i] = 0
            else:
                begin_matrix[i][j] = begin_matrix[j][i] = np.random.randint(1, 100)

    g = nx.Graph(begin_matrix)
    p = nx.spring_layout(g)
    e = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, p, e)
    nx.draw(g, p)
    plt.show()
    alg(begin_matrix, n, k)
