from general_liability import *


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

    def play_against_other_account(self, account):
        self.gl.play_business_line(account.gl)
