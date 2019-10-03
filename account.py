from general_liability import *
from property import *
from auto import *
import re


def is_def(n):
    if not n:
        return 6
    return int(n)


def parse_currency(s):
    return int(re.sub('[^\d.]', '', s))


class Account:
    def __init__(self, account):
        self.id = account['record']
        self.gl_weight_premium = parse_currency(account['gl_weight_premium'])
        self.p_weight_premium = parse_currency(account['p_weight_premium'])
        self.a_weight_premium = parse_currency(account['a_weight_premium'])
        self.total_premium = self.gl_weight_premium + self.p_weight_premium + self.a_weight_premium
        self.gl = GeneralLiability(self.gl_weight_premium,
                                   account['gl_indicated_premium_score'],
                                   is_def(account['gl_indicated_premium_points']),
                                   account['gl_exposure_size_score'],
                                   is_def(account['gl_exposure_size_points']),
                                   account['gl_yum_score'],
                                   is_def(account['gl_yum_points']),
                                   account['gl_osha_score'],
                                   is_def(account['gl_osha_points']),
                                   account['gl_teiring_industry_score'],
                                   is_def(account['gl_teiring_industry_points']),
                                   account['gl_hazard_class_score'],
                                   is_def(account['gl_hazard_class_points'])
                                   )
        self.property = Property(self.p_weight_premium,
                                 account['p_tiv_size_score'],
                                 is_def(account['p_tiv_size_point']),
                                 account['p_estimated_premium_score'],
                                 is_def(account['p_estimated_premium_point']),
                                 account['p_tiv_description_score'],
                                 is_def(account['p_tiv_description_point']),
                                 account['p_yum_score'],
                                 is_def(account['p_yum_point']),
                                 account['p_construction_grade_score'],
                                 is_def(account['p_construction_grade_point']),
                                 account['p_poor_construction_score'],
                                 is_def(account['p_poor_construction_point']),
                                 account['p_ppc_factor_score'],
                                 is_def(account['p_ppc_factor_point']),
                                 account['p_poor_ppc_score'],
                                 is_def(account['p_poor_ppc_point']),
                                 account['p_average_age_score'],
                                 is_def(account['p_average_age_point']),
                                 account['p_hurricane_premium_score'],
                                 is_def(account['p_hurricane_premium_point']),
                                 account['p_hurricane_dispersion_score'],
                                 is_def(account['p_hurricane_dispersion_point']),
                                 account['p_bg2_symbol_score'],
                                 is_def(account['p_bg2_symbol_point']),
                                 account['p_flood_premium_score'],
                                 is_def(account['p_flood_premium_point']),
                                 account['p_flood_dispersion_score'],
                                 is_def(account['p_flood_dispersion_point']),
                                 account['p_bad_flood_terr_score'],
                                 is_def(account['p_bad_flood_terr_point']),
                                 account['p_average_crime_score'],
                                 is_def(account['p_average_crime_point']),
                                 account['p_poor_crime_terr_score'],
                                 is_def(account['p_poor_crime_terr_point'])
                                 )
        self.auto = Auto(self.a_weight_premium,
                         account['a_indicated_single_vehicle_premium_score'],
                         is_def(account['a_indicated_single_vehicle_premium_point']),
                         account['a_indicated_total_premium_score'],
                         is_def(account['a_indicated_total_premium_point']),
                         account['a_NAICS_factor_score'],
                         is_def(account['a_NAICS_factor_point']),
                         account['a_primary_factor_score'],
                         is_def(account['a_primary_factor_point']),
                         account['a_crashes_score'],
                         is_def(account['a_crashes_point']),
                         )

    def play_against_other_account(self, account):
        combined_weight_premiums = self.total_premium + account.total_premium
        print('\nPlaying record {} vs. record {} with combined premiums {}'.format(self.id, account.id,
                                                                                   combined_weight_premiums))
        gl_weighted_total_points = self.gl.play_business_line(account.gl, combined_weight_premiums)
        property_weighted_total_points = self.property.play_business_line(account.property, combined_weight_premiums)
        auto_weighted_total_points = self.auto.play_business_line(account.auto, combined_weight_premiums)
        print('\n {}'.format(sum(self.gl.results + self.property.results + self.auto.results)))
        print('\n {} {} {}'.format(account.gl.results, account.property.results, account.auto.results))
