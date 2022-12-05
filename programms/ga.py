import random
import numpy as np

experiment = [4, -2, 3.5, 5, -11, -4.7]
Y = 35


def assessment(pop, y):
    p = []
    for i in range(len(pop)):
        s = 0
        for j in range(len(experiment)):
            s += pop[i][j] * experiment[j]
        r = np.abs(y - s) + 1
        p.append(1 / r)
    return p


def mut(p_after_co, rate):
    nextgen = []
    for i in range(0, len(p_after_co)):
        c = p_after_co[i]
        for j in range(len(c)):
            if random.random() < rate:
                random_value = np.random.uniform(-1.0, 1.0, 1)
                c[j] = c[j] + random_value
        nextgen.append(c)
    return nextgen


def co(parents, offspring_size):
    o = np.empty(offspring_size)
    co_point = np.uint8(offspring_size[1] / 2)
    for k in range(offspring_size[0]):
        p1 = k % len(parents)
        p2 = (k + 1) % len(parents)
        for i in range(co_point):
            o[k][i] = parents[p1][i]
        for i in range(co_point, offspring_size[1]):
            o[k][i] = parents[p2][i]
    return o


def parents_selection(population, parents_num, p):
    choose_parents = []
    for i in range(parents_num):
        max_ind = [j for j in range(len(p)) if p[j] == max(p)][0]
        choose_parents.append(population[max_ind])
        p.remove(max(p))
    return choose_parents


def results():
    w = len(experiment)
    sol = 12
    pop_size = (sol, w)
    new_pop = np.random.uniform(low=-len(experiment), high=len(experiment), size=pop_size)
    count_iteration = 10000
    for iteration in range(count_iteration):
        fitness = assessment(new_pop, Y)
        new_parents = parents_selection(new_pop, 6, fitness)
        new_offspring_cross = co(parents=new_parents,
                                 offspring_size=(pop_size[0] - len(new_parents), w))
        new_offspring_mut = mut(new_offspring_cross, 0.1)
        for i in range(len(new_parents)):
            new_pop[i] = new_parents[i]
        current_count = 0
        for i in range(len(new_parents), len(new_parents) + len(new_offspring_mut)):
            new_pop[i] = new_offspring_mut[current_count]
            current_count += 1
    fitness = assessment(new_pop, Y)
    max_fitness = max(fitness)
    print("Best Fitness: ", max_fitness)
    need_index = fitness.index(max_fitness)
    print("Best Chromosome: ", new_pop[need_index])


if __name__ == '__main__':
    results()
