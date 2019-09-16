import operator
import functools


class bColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


look_up = {
    -5: -1,
    -4: -0.5,
    -3: 0,
    -2: 0.5,
    -1: 1,
    0: 0,
    1: -1,
    2: -0.5,
    3: 0,
    4: 0.5,
    5: 1
}


class BaseField:
    def __init__(self, score, point):
        self.score = score
        self.point = point

    def play_field(self, point):
        if self.point == 6 or point == 6:
            return look_up[self.point-point]
        return self.point - point


class BaseLOB:
    def __init__(self):
        self.results = []
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def add_result(self, score):
        self.results.append(score)

    def add_win_loss(self, score):
        if score > 0:
            self.wins += 1
        elif score < 0:
            self.losses += 1
        else:
            self.ties += 0.5

    def process_score(self, score):
        self.add_win_loss(score)
        self.add_result(score)

    @property
    def score(self):
        return self.wins + self.ties


def sum_product(*lists):
    return sum(functools.reduce(operator.mul, data) for data in zip(*lists))
