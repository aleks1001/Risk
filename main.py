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
                     'p_tiv_description_score',
                     'p_yum_score',
                     'p_construction_grade_score',
                     'p_poor_construction_score',
                     'p_ppc_factor_score',
                     'p_poor_ppc_score',
                     'p_average_age_score',
                     'p_hurricane_premium_score',
                     'p_hurricane_dispersion_score',
                     'p_bg2_symbol_score',
                     'p_flood_premium_score',
                     'p_flood_dispersion_score',
                     'p_bad_flood_terr_score',
                     'p_average_crime_score',
                     'p_poor_crime_terr_score',
                     'p_tiv_size_point',
                     'p_estimated_premium_point',
                     'p_tiv_description_point',
                     'p_yum_point',
                     'p_construction_grade_point',
                     'p_poor_construction_point',
                     'p_ppc_factor_point',
                     'p_poor_ppc_point',
                     'p_average_age_point',
                     'p_hurricane_premium_point',
                     'p_hurricane_dispersion_point',
                     'p_bg2_symbol_point',
                     'p_flood_premium_point',
                     'p_flood_dispersion_point',
                     'p_bad_flood_terr_point',
                     'p_average_crime_point',
                     'p_poor_crime_terr_point']

csv_header_auto = [
    'a_indicated_single_vehicle_premium_score',
    'a_indicated_total_premium_score',
    'a_NAICS_factor_score',
    'a_primary_factor_score',
    'a_crashes_score',
    'a_indicated_single_vehicle_premium_point',
    'a_indicated_total_premium_point',
    'a_NAICS_factor_point',
    'a_primary_factor_point',
    'a_crashes_point']


class Risk:
    list = []

    def __init__(self, account):
        self.list.append(account)

    def print_all(self):
        for l in self.list:
            print('Record: ', l.id)
            print('\tGL:\t\t{:>2d} wins, {:>2d} loses, {:>5.2f} points'.format(l.gl.wins, l.gl.losses, l.gl.score))
            print('\tPROP:\t{:>2d} wins, {:>2d} loses, {:>5.2f} points'.format(l.property.wins, l.property.losses, l.property.score))

    def compare(self):
        for a, b in itertools.combinations(self.list, 2):
            print('\nPlaying record {} with record {}'.format(a.id, b.id))
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
        r = csv.DictReader(f, fieldnames=csv_header_list_gl + csv_header_list_p + csv_header_auto, dialect='excel')
        try:
            for row in r:
                # print(row)
                acc = Account(row)
                r = Risk(acc)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format('risk.csv', r.line_num, e))
    r.compare()
    r.print_all()


if __name__ == '__main__':
    main(sys.argv[1:])
