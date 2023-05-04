from time import sleep

from AI.Evaluator import evaluate
from AI.GameTree import game_tree
from AI.Policy import Policy, mate, mutate
from Game.GUI import Display
from Game.GameUI import GameUI
from random import random

def run_policy(policy, gui=False):
    game = GameUI()
    game.new_game()

    if gui:
        d = Display(game.get_board())

    while not game.isdone():
        positions_dict = game_tree(game)
        positions = list(positions_dict.keys())

        best_position = positions[0]
        best = policy.eval(evaluate(best_position.get_board()))

        for position in positions:
            position_b = position.get_board()
            observation = evaluate(position_b)
            eval = policy.eval(observation)
            if eval > best:
                best_position = position
                best = eval
        ind, cord = positions_dict[best_position]
        game.put_block(cord[0], cord[1], ind)

        if gui:
            d.update_window(game.score)
    return game.score

def get_random_genom(n):
    genom = []
    for i in range(n):
        n = random()*2 - 1
        genom.append(n)
    return genom

if __name__ == '__main__':
    n_population = 20
    population = [
        [-0.35312562071237885, -0.990981149625739, -0.2591653731111415, -0.24790698220920493, -0.0028962042989011394,
         -0.7186026832249471, -0.01938112076855214, -0.24730249591618647, -0.5867081462811695, -0.4287354641703167, 0, 0]]

    for _ in range(n_population - 1):
        population.append(mutate(population[0], 0.4, 0.3))

    batch = 20

    while True:
        score_board = []

        for ind, gen in enumerate(population):
            avg = 0
            for _ in range(batch):
                score = run_policy(Policy(gen),True)
                avg += score
            avg /= batch
            score_board.append((avg, gen))
            print(str(ind) + ". " + str(avg) + " <- " + str(gen))

        score_board.sort(key=lambda x:x[0], reverse=True)

        new_population = []
        for first in range(4):
            for second in range(first + 1, 4):
                new_population.append(mate(score_board[first][1], score_board[second][1]))
            new_population.append(score_board[first][1])

        for ind in range(10, n_population):
            chance = (2.5*ind - 10)/100.0
            mut = 0.3
            new_population.append(mutate(score_board[ind][1], chance, mut))

        population = new_population

# [-0.35312562071237885, -0.631549067070962, -0.2591653731111415, -0.24790698220920493, -0.0028962042989011394, -0.1586365295264448, -0.01938112076855214, -0.24730249591618647, -0.5867081462811695, -0.4287354641703167]