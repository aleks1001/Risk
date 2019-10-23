from base import BaseField, BaseLOB, sum_product


class IndicatedSingleVehiclePremium(BaseField):
    weight = 0.5

    def __init__(self, score, point):
        super().__init__(score, point)


class IndicatedTotalPremium(BaseField):
    weight = 1

    def __init__(self, score, point):
        super().__init__(score, point)


class NAICSFactor(BaseField):
    weight = 0.2

    def __init__(self, score, point):
        super().__init__(score, point)


class PrimaryFactor(BaseField):
    weight = 0.2

    def __init__(self, score, point):
        super().__init__(score, point)


class Crashes(BaseField):
    weight = 0.5

    def __init__(self, score, point):
        super().__init__(score, point)


class Auto(BaseLOB):
    def __init__(self,
                 weight_premium,
                 indicated_single_vehicle_premium_score,
                 indicated_single_vehicle_premium_point,
                 indicated_total_premium_score,
                 indicated_total_premium_point,
                 NAICS_factor_score,
                 NAICS_factor_point,
                 primary_factor_score,
                 primary_factor_point,
                 crashes_score,
                 crashes_point):
        super().__init__()
        self.weight_premium = weight_premium
        self.indicated_single_vehicle_premium = IndicatedSingleVehiclePremium(indicated_single_vehicle_premium_score,
                                                                              indicated_single_vehicle_premium_point)
        self.indicated_total_premium = IndicatedTotalPremium(indicated_total_premium_score,
                                                             indicated_total_premium_point)
        self.NAICS_factor = NAICSFactor(NAICS_factor_score, NAICS_factor_point)
        self.primary_factor = PrimaryFactor(primary_factor_score, primary_factor_point)
        self.crashes = Crashes(crashes_score, crashes_point)

    @property
    def weight_sum(self):
        return self.indicated_single_vehicle_premium.weight + \
               self.indicated_total_premium.weight + \
               self.NAICS_factor.weight + \
               self.primary_factor.weight + \
               self.crashes.weight

    def play_business_line(self, account):
        a = self.indicated_single_vehicle_premium.play_field(account.indicated_single_vehicle_premium.point)
        b = self.indicated_total_premium.play_field(account.indicated_total_premium.point)
        c = self.NAICS_factor.play_field(account.NAICS_factor.point)
        d = self.primary_factor.play_field(account.primary_factor.point)
        e = self.crashes.play_field(account.crashes.point)

        points = [a, b, c, d, e]
        weights = [self.indicated_single_vehicle_premium.weight,
                   self.indicated_total_premium.weight,
                   self.NAICS_factor.weight,
                   self.primary_factor.weight,
                   self.crashes.weight]

        # divide sum of product by weights sum
        p = sum_product(points, weights) / self.weight_sum
        self.process_point(p)
        account.process_point(p * -1)
        return p

    def print_results(self, s1, p1, s2, p2, weights):
        print('AUTO: {} vs. {}, '
              'with result: {} vs. {}, weights: {} with sum: {}'
              .format(s1, s2,
                      format(p1,
                             '.2f'),
                      format(p2,
                             '.2f'),
                      weights,
                      format(self.weight_sum, '.2f')))