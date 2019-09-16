import csv
import sys
import getopt
import itertools
from account import *

csv_header_list_gl = ['record',
                      'gl_indicated_premium_score',
                      'gl_exposure_size_score',
                      'gl_yum_score',
                      'gl_osha_score',
                      'gl_teiring_industry_score',
                      'gl_hazard_class_score',
                      'gl_indicated_premium_points',
                      'gl_exposure_size_points',
                      'gl_yum_points',
                      'gl_osha_points',
                      'gl_teiring_industry_points',
                      'gl_hazard_class_points']

csv_header_list_p = ['p_tiv_size_score',
                     'p_estimated_premium_score',
                     'p_tiv_description_score']


class Risk:
    list = []

    def __init__(self, account):
        self.list.append(account)

    def print_all(self):
        for l in self.list:
            print('Record: {} has {} wins and {} loses with total score {}'.format(l.id, l.gl.wins, l.gl.losses,
                                                                                   l.gl.score))

    def compare(self):
        for a, b in itertools.combinations(self.list, 2):
            print('Playing record {} with record {}'.format(a.id, b.id))
            a.play_against_other_account(b)


def parse_args(argv):
    input_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is "', inputfile)
    print('Output file is "', outputfile)


def main(argv):
    print("Parsing {}".format(argv[0]))
    with open(argv[0]) as f:
        r = csv.DictReader(f, fieldnames=csv_header_list_gl + csv_header_list_p, dialect='excel')
        try:
            next(r)
            for row in r:
                print(row)
                # acc = Account(row)
                # r = Risk(acc)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format('risk.csv', r.line_num, e))
    # r.compare()
    # r.print_all()


if __name__ == '__main__':
    main(sys.argv[1:])
