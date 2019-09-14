import csv
import sys
import itertools
from account import *


class Risk:
    list = []

    def __init__(self, account):
        self.list.append(account)

    def print_all(self):
        for l in self.list:
            print(len(l.gl.results), 'wins: ', l.gl.wins, 'loses: ', l.gl.losses)

    def compare(self):
        for a, b in itertools.combinations(self.list[0:6], 2):
            print('Playing record {} with record {}'.format(a.id, b.id))
            a.play_against_other_account(b)


def main():
    print("Parsing {}".format(sys.argv[1]))
    with open(sys.argv[1]) as f:
        r = csv.DictReader(f, dialect='excel')
        try:
            for row in r:
                acc = Account(row)
                r = Risk(acc)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format('risk.csv', r.line_num, e))
    r.compare()
    # r.print_all()


if __name__ == '__main__':
    main()
