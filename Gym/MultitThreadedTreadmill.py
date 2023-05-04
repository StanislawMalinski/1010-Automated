from AI.Policy import mate, mutate
from Gym.Thread import TreadmillThread
from Gym.Treadmill import get_random_genom

if __name__ == '__main__':
    n_population = 20
    population = [[-0.35312562071237885, -0.990981149625739, -0.2591653731111415, -0.24790698220920493, -0.0028962042989011394, -0.7186026832249471, -0.01938112076855214, -0.24730249591618647, -0.5867081462811695, -0.4287354641703167,0,0]]

    for _ in range(n_population-1):
        population.append(get_random_genom(12))

    batch = 20

    while True:
        score_board = []

        threads = []
        for gen in population:
            t = TreadmillThread(gen, batch)
            threads.append(t)
            t.start()

        not_done = True
        while not_done:
            not_done = False
            for t in threads:
                if not t.is_alive() and not t.read:
                    t.join()
                    score_board.append((t.avg, t.genom))
                    print(str(t.avg) + " <- " + str(t.genom))
                    t.read = True
                else:
                    not_done = True

        score_board.sort(key=lambda x: x[0], reverse=True)

        new_population = []
        for first in range(4):
            for second in range(first + 1, 4):
                new_population.append(mate(score_board[first][1], score_board[second][1]))
            new_population.append(score_board[first][1])

        for ind in range(10, n_population):
            chance = (2.5 * ind - 10) / 100.0
            mut = 0.3
            new_population.append(mutate(score_board[ind][1], chance, mut))

        population = new_population