from threading import Thread

from AI.Policy import Policy
from Gym.Treadmill import run_policy


class TreadmillThread(Thread):
    def __init__(self, p, batch, gui=False):
        super().__init__()
        self.genom = p
        self.gui = gui
        self.batch = batch
        self.avg = 0
        self.read = False

    def run(self):
        for _ in range(self.batch):
            self.avg += run_policy(Policy(self.genom), self.gui)
        self.avg /= self.batch
        self.read = False
