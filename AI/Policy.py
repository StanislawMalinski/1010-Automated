from random import random

class Policy:
    def __init__(self, gen: list):
        self.gen = gen
        self.n = len(gen)

    def eval(self, observation):
        ev = self.gen.copy()
        sum = 0
        for ind, param in enumerate(observation):
            sum += ev[ind] * param
        return sum  # 1 -> bardzo dobra pozycja, -1 -> bardzo nie dobra pozycja

def mutate(gen, chance, mut):  # chance <0, 1>, mut <0, 1>
    n_gen = gen.copy()
    n = len(n_gen)
    for i in range(n):
        if random() <= chance:
            a = (2 * random() - 1) * mut
            n_gen[i] = max(n_gen[i] + a, -1)
            n_gen[i] = min(n_gen[i] + a, 1)
    return n_gen

def mate(gen1, gen2):  # other Policy
    n_gen = gen1.copy()
    n = len(n_gen)
    for i in range(n):
        if random() >= 0.5:
            n_gen[i] = gen2[i]
    return n_gen

