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


class BaseField:
    def __init__(self, score, point):
        self.score = score
        self.point = point

    def play_field(self, point):
        return self.point - point


class BaseLOB:
    def __init__(self):
        self.results = []
        self.wins = 0
        self.losses = 0

    def add_result(self, score):
        self.results.append(score)

    def add_win_loss(self, score):
        if score > 0:
            self.wins += 1
        else:
            self.losses += 1

    def process_score(self, score):
        self.add_win_loss(score)
        self.add_result(score)


def sum_product(*lists):
    return sum(functools.reduce(operator.mul, data) for data in zip(*lists))
