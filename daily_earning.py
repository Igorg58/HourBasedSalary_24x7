from common_data import rate_base


class DailyEarn(object):
    def __init__(self, type_, hours, **kwargs):
        self.type = type_
        self.hours = hours
        self.extra_hours = {'h_125': 0, 'h_150': 0, 'h_175': 0, 'h_200': 0}
        self.extra_hours.update(kwargs)

    def daily_salary(self):
        percent_key2add_coef = {'h_125': 0.25, 'h_150': 0.5, 'h_175': 0.75, 'h_200': 1}
        daily = rate_base * self.hours
        for percent_key, num_h in self.extra_hours.items():
            daily += num_h * rate_base * percent_key2add_coef[percent_key]
        return daily

    def get_hours_num(self):
        return self.hours

    def get_extra_hours(self):
        return self.extra_hours


class DailyEarnTypes(object):
    """
    Collection of all possible instances of DailyEarn according to hours number and extra hours.
    Extra hours depend on day-of-week (regular / shabbat (holiday))EE```, hours number, day / night.
    """
    regular_morning_8 = DailyEarn('regular_morning_8', 8)  # 7-15
    regular_evening_8 = DailyEarn('regular_evening_8',8)  # 15-23
    regular_night_8 = DailyEarn('regular_night_8',8, h_125=1)  # 23-7
    regular_night_7 = DailyEarn('regular_night_7',7)  # 24-7

    friday_morning_8 = DailyEarn('friday_morning_8',8)  # 7-15
    friday_evening_8 = DailyEarn('friday_evening_8',8, h_150=4)  # 15-23
    friday_night_8 = DailyEarn('friday_night_8',8, h_150=7, h_175=1)  # 23-6, 6-7
    friday_morning_12 = DailyEarn('friday_morning_12',12, h_125=2, h_150=2)    # 7-15, 15-17, 17-19
    friday_night_12 = DailyEarn('friday_night_12', 12, h_150=7, h_175=2, h_200=3)  # 19-2, 2-4, 4-7

    saturday_morning_8 = DailyEarn('saturday_morning_8',8, h_150=8)  # 7-15
    saturday_evening_8 = DailyEarn('saturday_evening_8',8, h_150=8)  # 15-23
    saturday_night_8 = DailyEarn('saturday_night_8',8, h_125=1)  # 23-6, 6-7
    saturday_morning_12 = DailyEarn('saturday_morning_12',12, h_150=8, h_175=2, h_200=2)  # 7-15, 15-17, 17-19
    saturday_night_12 = DailyEarn('saturday_night_12',12, h_125=2, h_150=3)  # 19-2, 2-4, 4-7

    extra_1h_175 = DailyEarn('extra_1h_175',1, h_175=1)


    @staticmethod
    def get_types_and_salary():
        types_and_salary = [
            '=' * 10 + ' Common info:types and salary ' + '=' * 10 + '\n',
            f'Base rate = {rate_base}\n'
            f'Regular morning 8 = {DailyEarnTypes.regular_morning_8.daily_salary():.2f}\n',
            f'Regular evening 8 = {DailyEarnTypes.regular_evening_8.daily_salary():.2f}\n',
            f'Regular night 8 = {DailyEarnTypes.regular_night_8.daily_salary():.2f}\n',
            f'Regular night 7 = {DailyEarnTypes.regular_night_7.daily_salary():.2f}\n',
            f'Friday morning 8 = {DailyEarnTypes.friday_morning_8.daily_salary():.2f}\n',
            f'Friday evening 8 = {DailyEarnTypes.friday_evening_8.daily_salary():.2f}\n',
            f'Friday night 8 = {DailyEarnTypes.friday_night_8.daily_salary():.2f}\n',
            f'Friday morning 12 = {DailyEarnTypes.friday_morning_12.daily_salary():.2f}\n',
            f'Friday night 12 = {DailyEarnTypes.friday_night_12.daily_salary():.2f}\n',
            f'Saturday morning 8 = {DailyEarnTypes.saturday_morning_8.daily_salary():.2f}\n',
            f'Saturday evening 8 = {DailyEarnTypes.saturday_evening_8.daily_salary():.2f}\n',
            f'Saturday night 8 = {DailyEarnTypes.saturday_night_8.daily_salary():.2f}\n',
            f'Saturday morning 12 = {DailyEarnTypes.saturday_morning_12.daily_salary():.2f}\n',
            f'Saturday night 12 = {DailyEarnTypes.saturday_night_12.daily_salary():.2f}\n',
            f'Extra working 1 hour with 175% = {DailyEarnTypes.extra_1h_175.daily_salary():.2f}\n',
            # '=' * 40,
            '\n'
        ]
        return types_and_salary
