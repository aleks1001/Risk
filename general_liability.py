from base import BaseField, BaseLOB, sum_product


class IndicatedPremium(BaseField):
    weight = 1

    def __init__(self, score, point):
        super().__init__(score, point)


class ExposureSize(BaseField):
    weight = 0.25

    def __init__(self, score, point):
        super().__init__(score, point)


class Yum(BaseField):
    weight = 0.15

    def __init__(self, score, point):
        super().__init__(score, point)


class Osha(BaseField):
    weight = 0

    def __init__(self, score, point):
        super().__init__(score, point)


class TeiringIndustry(BaseField):
    weight = 0.2

    def __init__(self, score, point):
        super().__init__(score, point)


class HazardClass(BaseField):
    weight = 0.35

    def __init__(self, score, point):
        super().__init__(score, point)


class GeneralLiability(BaseLOB):
    def __init__(self,
                 weight_premium,
                 indicated_premium_score,
                 indicated_premium_points,
                 exposure_size_score,
                 exposure_size_points,
                 yum_score,
                 yum_points,
                 osha_score,
                 osha_points,
                 teiring_ind_score,
                 teiring_ind_points,
                 hazard_class_score,
                 hazard_class_points):
        super().__init__()
        self.weight_premium = weight_premium
        self.indicated_premium = IndicatedPremium(indicated_premium_score, indicated_premium_points)
        self.exposure_size = ExposureSize(exposure_size_score, exposure_size_points)
        self.yum = Yum(yum_score, yum_points)
        self.osha = Osha(osha_score, osha_points)
        self.teiring_industry = TeiringIndustry(teiring_ind_score, teiring_ind_points)
        self.hazard_class = HazardClass(hazard_class_score, hazard_class_points)

    @property
    def weight_sum(self):
        return self.indicated_premium.weight + \
               self.exposure_size.weight + \
               self.yum.weight + \
               self.osha.weight + \
               self.teiring_industry.weight + \
               self.hazard_class.weight

    def play_business_line(self, account, premiums):
        a = self.indicated_premium.play_field(account.indicated_premium.point)
        b = self.exposure_size.play_field(account.exposure_size.point)
        c = self.yum.play_field(account.yum.point)
        d = self.osha.play_field(account.osha.point)
        e = self.teiring_industry.play_field(account.teiring_industry.point)
        f = self.hazard_class.play_field(account.hazard_class.point)

        points = [a, b, c, d, e, f]
        weights = [self.indicated_premium.weight,
                   self.exposure_size.weight,
                   self.yum.weight,
                   self.osha.weight,
                   self.teiring_industry.weight,
                   self.hazard_class.weight]

        # divide sum of product by weights sum
        total_points = sum_product(points, weights) / self.weight_sum
        self.process_score(total_points * (self.weight_premium/premiums))
        account.process_score(total_points * (account.weight_premium/premiums) * -1)
        self.print_results(points, total_points, list(map(lambda x: x * -1, points)), total_points * -1, weights)

    def print_results(self, s1, p1, s2, p2, weights):
        print('GL: {} vs. {}, '
              'with result: {} vs. {}, weights: {} with sum: {}'
              .format(s1, s2,
                      format(p1,
                             '.2f'),
                      format(p2,
                             '.2f'),
                      weights,
                      format(self.weight_sum, '.2f')))
