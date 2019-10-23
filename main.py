import csv
import sys
import getopt
import itertools
from account import *

csv_header_list_gl = ['gl_weight_premium',
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

csv_header_list_p = ['p_weight_premium',
                     'p_tiv_size_score',
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
    'a_weight_premium',
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


class Accounts:
    list = []
    account_to_run = 0

    def __init__(self, argv):
        super().__init__()
        try:
            opts, args = getopt.getopt(argv, "i:o:n:", ['ifile=', 'ofile='])
        except getopt.GetoptError:
            print('main.py -n <accounts_to_run> -i <inputfile> -o <outputfile>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('main.py -n <accounts_to_run> -i <inputfile> -o <outputfile>')
                sys.exit()
            elif opt in ("-i", "--ifile"):
                self.input_file = arg
            elif opt in ("-o", "--ofile"):
                self.output_file = arg
            elif opt == '-n':
                self.account_to_run = int(arg)

    def read_csv(self):
        with open(self.input_file) as file:
            r = csv.DictReader(file,
                               fieldnames=['record'] + csv_header_list_gl + csv_header_list_p + csv_header_auto,
                               dialect='excel')
            next(r)
            try:
                for row in r:
                    acc = Account(row)
                    self.list.append(acc)
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format('risk.csv', r.line_num, e))

    def write_csv(self):
        with open(self.output_file, 'w', newline='') as file:
            fields = ['id', 'total_scores', 'total_points', 'total_win_lose',
                      'gl_scores', 'gl_points', 'gl_win_loss',
                      'p_scores', 'p_points', 'p_win_loss',
                      'a_scores', 'a_points', 'a_win_loss']
            w = csv.DictWriter(file, fieldnames=fields, dialect='excel')
            w.writeheader()
            for a in self.list[0:self.account_to_run]:
                w.writerow({'id': a.id,
                            'total_scores': a.score_total,
                            'total_points': format(a.point_total, '.2f'),
                            'total_win_lose': a.result_total,
                            'gl_scores': a.gl.score,
                            'gl_points': format(a.gl.point, '.2f'),
                            'gl_win_loss': format(a.gl.result, '.2f'),
                            'p_scores': a.property.score,
                            'p_points': format(a.property.point, '.2f'),
                            'p_win_loss': format(a.property.result, '.2f'),
                            'a_scores': a.auto.score,
                            'a_points': format(a.auto.point, '.2f'),
                            'a_win_loss': format(a.auto.result, '.2f')
                            })

    def print(self):
        print('\n{} \t{} \t{} \t{} \t{} \t{} \t{} \t{} \t{} \t{} \t{} \t{} \t{}'.format('Record', 'Total scores',
                                                                                        'Total points',
                                                                                        'Total win/lose', 'GL scores',
                                                                                        'GL points',
                                                                                        'GL win/loss', 'P scores',
                                                                                        'P points', 'P win/loss',
                                                                                        'A scores',
                                                                                        'A points', 'A win/loss'))
        for a in self.list[0:self.account_to_run]:
            print(
                '{:>3s} \t{:>6d} \t{:>16.2f} \t{:>11.1f} \t{:>10d} \t{:>12.2f} \t{:>9.1f} \t{:>8d} \t{:>10.2f} \t{:>11.1f} \t{:>5d} \t{:>11.2f} \t{:>8.1f}'.format(
                    a.id,
                    0,
                    a.point_total,
                    a.result_total,
                    a.gl.score,
                    a.gl.point,
                    a.gl.result,
                    a.property.score,
                    a.property.point,
                    a.property.result,
                    a.auto.score,
                    a.auto.point,
                    a.auto.result))

    def play(self):
        for a, b in itertools.combinations(self.list[0:self.account_to_run], 2):
            a.play_against_other_account(b)

    def show_results(self, record_id):
        acc = self.list[record_id]
        print('\n{}'.format(acc.addition_info.account_against))


def main(argv):
    accounts = Accounts(argv)
    accounts.read_csv()
    accounts.play()
    accounts.print()
    accounts.write_csv()
    # accounts.show_results(10)


if __name__ == '__main__':
    main(sys.argv[1:])
