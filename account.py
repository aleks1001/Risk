from general_liability import *
from property import *


def is_def(n):
    if not n:
        return 6
    return int(n)


class Account:
    def __init__(self, account):
        self.id = account['record']
        self.gl = GeneralLiability(account['gl_indicated_premium_score'],
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
        self.property = Property(account['p_tiv_size_score'],
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

    def play_against_other_account(self, account):
        self.gl.play_business_line(account.gl)
        self.property.play_business_line(account.property)
