import random

import numpy
import numpy as np

EXPERIMENT = [8, -1, 6, 7, -9, -7]
Y = 60
weights = len(EXPERIMENT)
C = 6
SIZE = (C, weights)
POP = np.random.randint(low=-len(EXPERIMENT), high=len(EXPERIMENT), size=SIZE)
ITERATION = 3000


def fit(population, y):
    pop = []
    for i in range(len(population)):
        s = 0
        for j in range(len(EXPERIMENT)):
            s += population[i][j] * EXPERIMENT[j]
        r = np.abs(y - s) + 1
        pop.append(1 / r)
    return pop


def result():
    for iteration in range(ITERATION):
        fitness = fit(POP, Y)
        new_parents = selection(POP, 6, fitness)
        new_c_co = co(parents=new_parents, size=(SIZE[0] - len(new_parents), weights))
        new_off_mut = mut(new_c_co, 0.1)
        for i in range(len(new_parents)):
            POP[i] = new_parents[i]
        count = 0
        for i in range(len(new_parents), len(new_parents) + len(new_off_mut)):
            POP[i] = new_off_mut[count]
            count += 1
    fitness = fit(POP, Y)
    max_f = max(fitness)
    index = fitness.index(max_f)
    print("The best chromosome: ", POP[index])
    index_best = numpy.where(fitness == numpy.max(fitness))
    print(fitness)
    print(index_best)
    print(POP)
    print(POP[index_best, :])


def selection(pop, number, p):
    parents = []
    for i in range(number):
        max_ind = [j for j in range(len(p)) if p[j] == max(p)][0]
        parents.append(pop[max_ind])
        p.remove(max(p))
    return parents


def co(parents, size):
    off = np.empty(size)
    point = np.uint8(size[1] / 2)
    for k in range(size[0]):
        p1 = k % len(parents)
        p2 = (k + 1) % len(parents)
        for i in range(point):
            off[k][i] = parents[p1][i]

        for i in range(point, size[1]):
            off[k][i] = parents[p2][i]
    return off


def mut(after_c, mutation):
    p = []
    for i in range(0, len(after_c)):
        chrom = after_c[i]
        for j in range(len(chrom)):
            if random.random() < mutation:
                random_value = np.random.randint(-1.0, 1.0, 1)
                chrom[j] = chrom[j] + random_value
        p.append(chrom)
    return p


if __name__ == '__main__':
    result()
