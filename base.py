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
            return look_up[self.point - point]
        return self.point - point


class BaseLOB:
    def __init__(self):
        self.points = []
        self.scores = []
        self.results = []

    def add_points(self, point):
        self.points.append(point)

    def add_results(self, result):
        self.results.append(result)

    def add_scores(self, score):
        self.scores.append(score)

    def process_point(self, point):
        self.add_points(point)
        if point > 0:
            self.add_results(1)
        elif point < 0:
            self.add_results(0)
        else:
            self.add_results(0.5)

    @property
    def score(self):
        return sum(self.scores)

    @property
    def point(self):
        return sum(self.points)

    @property
    def result(self):
        return sum(self.results)


def sum_product(*lists):
    return sum(functools.reduce(operator.mul, data) for data in zip(*lists))
