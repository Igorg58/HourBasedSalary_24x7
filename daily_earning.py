from common_data import rate_base


class DailyEarn(object):
    def __init__(self, hours, **kwargs):
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
    day_regular = DailyEarn(8)
    # print(f'Regular 8 = {day_regular.daily_salary()}')

    friday_morning_8 = DailyEarn(8)
    # print(f'Friday 8 morning = {friday_morning_8.daily_salary():.2f}')

    friday_evening_8 = DailyEarn(8, h_150=4)
    # print(f'Friday 8 evening = {friday_evening_8.daily_salary():.2f}')

    friday_morning_12 = DailyEarn(12, h_125=2, h_150=2)
    # print(f'Friday 12 morning = {friday_morning_12.daily_salary():.2f}')

    saturday_morning_8 = DailyEarn(8, h_150=8)
    # print(f'Saturday 8 morning = {saturday_morning_8.daily_salary():.2f}')

    saturday_evening_8 = DailyEarn(8, h_150=8)
    # print(f'Saturday 8 evening = {saturday_evening_8.daily_salary():.2f}')

    saturday_morning_12 = DailyEarn(12, h_150=8, h_175=2, h_200=2)  # 7 - 15, 15 - 17, 17 -19
    # print(f'Saturday 12 morning = {saturday_morning_12.daily_salary():.2f}')

    night_regular = DailyEarn(8, h_125=1)  # 23-7
    # print(f'Night regular = {night_regular.daily_salary():.2f}')

    night_7 = DailyEarn(7)  # 0-7
    # print(f'Night 7 = {night_7.daily_salary():.2f}')

    friday_night_8 = DailyEarn(8, h_150=7, h_175=1)  # 23-6, 6-7
    # print(f'Friday night 8 = {friday_night_8.daily_salary():.2f}')

    saturday_night_8 = DailyEarn(8, h_125=1)  # 23-6, 6-7
    # print(f'Saturday night 8 = {saturday_night_8.daily_salary():.2f}')

    friday_night_12 = DailyEarn(12, h_150=7, h_175=2, h_200=3)  # 19-2, 2-4, 4-7
    # print(f'Friday night 12 = {friday_night_12.daily_salary():.2f}')

    saturday_night_12 = DailyEarn(12, h_125=2, h_150=3)
    # print(f'Saturday night 12 = {saturday_night_12.daily_salary():.2f}')

    extra_1h_175 = DailyEarn(1, h_175=1)
    # print(f'Extra working 1 hour with 175% = {extra_1h_175.daily_salary():.2f}')

    # print('=' * 40 )

    @staticmethod
    def get_types_and_salary():
        types_and_salary = [
            '=' * 10 + ' Types and salary ' + '=' * 10 + '\n'
            f'Regular 8 = {DailyEarnTypes.day_regular.daily_salary():.2f}\n',
            f'Friday 8 morning = {DailyEarnTypes.friday_morning_8.daily_salary():.2f}\n',
            f'Friday 8 evening = {DailyEarnTypes.friday_evening_8.daily_salary():.2f}\n',
            f'Friday 12 morning = {DailyEarnTypes.friday_morning_12.daily_salary():.2f}\n',
            f'Saturday 8 morning = {DailyEarnTypes.saturday_morning_8.daily_salary():.2f}\n',
            f'Saturday 8 evening = {DailyEarnTypes.saturday_evening_8.daily_salary():.2f}\n',
            f'Saturday 12 morning = {DailyEarnTypes.saturday_morning_12.daily_salary():.2f}\n',
            f'Night regular = {DailyEarnTypes.night_regular.daily_salary():.2f}\n',
            f'Night 7 = {DailyEarnTypes.night_7.daily_salary():.2f}\n',
            f'Friday night 8 = {DailyEarnTypes.friday_night_8.daily_salary():.2f}\n',
            f'Saturday night 8 = {DailyEarnTypes.saturday_night_8.daily_salary():.2f}\n',
            f'Friday night 12 = {DailyEarnTypes.friday_night_12.daily_salary():.2f}\n',
            f'Saturday night 12 = {DailyEarnTypes.saturday_night_12.daily_salary():.2f}\n',
            f'Extra working 1 hour with 175% = {DailyEarnTypes.extra_1h_175.daily_salary():.2f}\n',
            # '=' * 40,
            '\n'
        ]
        return types_and_salary
