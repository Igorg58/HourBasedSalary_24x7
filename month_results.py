import os
import sys
import importlib
from daily_earning import DailyEarnTypes


def month_results(month: str, year: str):
    cwd = os.getcwd()
    config_path = os.path.join(cwd, 'Config')
    if config_path not in sys.path:
        sys.path.insert(0, config_path)
    monthly_config_module = importlib.import_module(f'config_{month}_{year}')

    output_file_path = os.path.join('Output', f'salary_{month}_{year}.txt')
    fp = open(output_file_path, 'w')
    types_and_salary = DailyEarnTypes.get_types_and_salary()
    fp.writelines(types_and_salary)

    working_days = {}
    for date, typ in monthly_config_module.working_dates_and_types.items():
        working_days.update({date: getattr(DailyEarnTypes, typ)})

    print('=' * 10 + ' Dates earning ' + '=' * 10)
    fp.write('=' * 10 + ' Dates earning ' + '=' * 10 + '\n')
    salary = 0
    day_of_month = '00'
    days = 0
    all_hours = 0
    extra_hours = {'h_125': 0, 'h_150': 0, 'h_175': 0, 'h_200': 0}
    for date, earn_daily in working_days.items():
        print(f'{date}: {earn_daily.daily_salary():.2f}')
        fp.write(f'{date}: {earn_daily.daily_salary():.2f}\n')
        salary += earn_daily.daily_salary()
        day_of_month_candidate = date.split('.')[0]
        if day_of_month not in day_of_month_candidate:
            days += 1
        day_of_month = day_of_month_candidate

        all_hours += earn_daily.get_hours_num()
        daily_extra_hours = earn_daily.get_extra_hours()
        for key, val in daily_extra_hours.items():
            extra_hours[key] += daily_extra_hours[key]  # the same as above

    print('\n' + '=' * 10 + ' Summary ' + '=' * 10)
    fp.write('\n' + '=' * 10 + ' Summary ' + '=' * 10 + '\n')

    print(f'Salary month = {salary:.2f}')
    fp.write(f'Salary month = {salary:.2f}\n')

    print(f'Working days  = {len(working_days)}')
    fp.write(f'Working days  = {len(working_days)}\n')

    print(f'All hours = {all_hours}')
    fp.write(f'All hours = {all_hours}\n')

    # print(f'extra hours = {extra_hours}')  # TODO: human print
    verbal_extra_hours = {key.split('_')[1]+'%': val for (key, val) in extra_hours.items()}  # human print
    print(f'extra hours = {verbal_extra_hours}')
    fp.write(f'extra hours = {verbal_extra_hours}\n')
    fp.close()
