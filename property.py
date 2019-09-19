from base import BaseField, BaseLOB, sum_product


class TIVSize(BaseField):
    weight = 0.50

    def __init__(self, score, point):
        super().__init__(score, point)


class EstimatedPremium(BaseField):
    weight = 1

    def __init__(self, score, point):
        super().__init__(score, point)


class TIVDescription(BaseField):
    weight = 0.35

    def __init__(self, score, point):
        super().__init__(score, point)


class YUM(BaseField):
    weight = 0.1

    def __init__(self, score, point):
        super().__init__(score, point)


class ConstructionGrade(BaseField):
    weight = 0.1

    def __init__(self, score, point):
        super().__init__(score, point)


class PoorConstruction(BaseField):
    weight = 0.1

    def __init__(self, score, point):
        super().__init__(score, point)


class PPCFactor(BaseField):
    weight = 0.1

    def __init__(self, score, point):
        super().__init__(score, point)


class PoorPPC(BaseField):
    weight = 0.15

    def __init__(self, score, point):
        super().__init__(score, point)


class AverageAge(BaseField):
    weight = 0.15

    def __init__(self, score, point):
        super().__init__(score, point)


class HurricanePremium(BaseField):
    weight = 0.15

    def __init__(self, score, point):
        super().__init__(score, point)


class HurricaneDescription(BaseField):
    weight = 0.15

    def __init__(self, score, point):
        super().__init__(score, point)


class BG2Symbol(BaseField):
    weight = 0

    def __init__(self, score, point):
        super().__init__(score, point)


class FloodPremium(BaseField):
    weight = 0.15

    def __init__(self, score, point):
        super().__init__(score, point)


class FloodDescription(BaseField):
    weight = 0.15

    def __init__(self, score, point):
        super().__init__(score, point)


class BadFloodTerr(BaseField):
    weight = 0.15

    def __init__(self, score, point):
        super().__init__(score, point)


class AverageCrime(BaseField):
    weight = 0.1

    def __init__(self, score, point):
        super().__init__(score, point)


class PoorCrimeTerr(BaseField):
    weight = 0.15

    def __init__(self, score, point):
        super().__init__(score, point)


class Property(BaseLOB):
    def __init__(self,
                 tiv_size_score,
                 tiv_size_point,
                 estimated_premium_score,
                 estimated_premium_point,
                 tiv_description_score,
                 tiv_description_point,
                 yum_score,
                 yum_point,
                 construction_grade_score,
                 construction_grade_point,
                 poor_construction_score,
                 poor_construction_point,
                 ppc_factor_score,
                 ppc_factor_point,
                 poor_ppc_score,
                 poor_ppc_point,
                 average_age_score,
                 average_age_point,
                 hurricane_premium_score,
                 hurricane_premium_point,
                 hurricane_dispersion_score,
                 hurricane_dispersion_point,
                 bg2_symbol_score,
                 bg2_symbol_point,
                 flood_premium_score,
                 flood_premium_point,
                 flood_dispersion_score,
                 flood_dispersion_point,
                 bad_flood_terr_score,
                 bad_flood_terr_point,
                 average_crime_score,
                 average_crime_point,
                 poor_crime_terr_score,
                 poor_crime_terr_point
                 ):
        super().__init__()
        self.tiv_size = TIVSize(tiv_size_score, tiv_size_point)
        self.estimated_premium = EstimatedPremium(estimated_premium_score, estimated_premium_point)
        self.tiv_description = TIVDescription(tiv_description_score, tiv_description_point)
        self.yum = YUM(yum_score, yum_point)
        self.construction_grade = ConstructionGrade(construction_grade_score, construction_grade_point)
        self.poor_construction = ConstructionGrade(poor_construction_score, poor_construction_point)
        self.ppc_factor = PPCFactor(ppc_factor_score, ppc_factor_point)
        self.poor_ppc = PoorPPC(poor_ppc_score, poor_ppc_point)
        self.average_age = AverageAge(average_age_score, average_age_point)
        self.hurricane_premium = HurricanePremium(hurricane_premium_score, hurricane_premium_point)
        self.hurricane_dispersion = HurricaneDescription(hurricane_dispersion_score, hurricane_dispersion_point)
        self.bg2_symbol = BG2Symbol(bg2_symbol_score, bg2_symbol_point)
        self.flood_premium = FloodPremium(flood_premium_score, flood_premium_point)
        self.flood_dispersion = FloodDescription(flood_dispersion_score, flood_dispersion_point)
        self.bad_flood_terr = BadFloodTerr(bad_flood_terr_score, bad_flood_terr_point)
        self.average_crime = AverageCrime(average_crime_score, average_crime_point)
        self.poor_crime_terr = PoorCrimeTerr(poor_crime_terr_score, poor_crime_terr_point)

    @property
    def weight_sum(self):
        return self.tiv_size.weight + \
               self.estimated_premium.weight + \
               self.tiv_description.weight + \
               self.yum.weight + \
               self.construction_grade.weight + \
               self.poor_construction.weight + \
               self.ppc_factor.weight + \
               self.poor_ppc.weight + \
               self.average_age.weight + \
               self.hurricane_premium.weight + \
               self.hurricane_dispersion.weight + \
               self.bg2_symbol.weight + \
               self.flood_premium.weight + \
               self.flood_dispersion.weight + \
               self.bad_flood_terr.weight + self.average_crime.weight + self.poor_crime_terr.weight

    def play_business_line(self, account):
        a = self.tiv_size.play_field(account.tiv_size.point)
        b = self.estimated_premium.play_field(account.estimated_premium.point)
        c = self.tiv_description.play_field(account.tiv_description.point)
        d = self.yum.play_field(account.yum.point)
        e = self.construction_grade.play_field(account.construction_grade.point)
        f = self.poor_construction.play_field(account.poor_construction.point)

        scores = [a, b, c, d, e, f]
        weights = [self.tiv_size.weight,
                   self.estimated_premium.weight,
                   self.tiv_description.weight,
                   self.yum.weight,
                   self.construction_grade.weight,
                   self.poor_construction.weight]

        # divide sum of product by weights sum
        prod = sum_product(scores, weights) / self.weight_sum

        self.process_score(prod)
        account.process_score(prod * -1)
        self.print_results(scores, prod, list(map(lambda x: x * -1, scores)), prod * -1, weights)

    def print_results(self, s1, p1, s2, p2, weights):
        print('{} vs. {}, '
              'with result: {} vs. {}, weights: {} with sum: {}'
              .format(s1, s2,
                      format(p1,
                             '.2f'),
                      format(p2,
                             '.2f'),
                      weights,
                      format(self.weight_sum, '.2f')))