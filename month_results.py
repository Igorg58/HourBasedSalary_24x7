import os
import sys
import importlib
from daily_earning import DailyEarnTypes
from config_csv_processing import config_csv_processing


def month_results(month: str, year: str):
    # Write common info about salary for possible samples of types
    output_exist = os.path.isdir('Output')
    if not output_exist:
        os.mkdir('Output')
    output_file_path = os.path.join('Output', f'salary_{month}_{year}.txt')
    fp = open(output_file_path, 'w')
    types_salary_samples = DailyEarnTypes.get_types_and_salary()
    fp.writelines(types_salary_samples)

    # Try use 'config_<mm>_<YY>.csv' rawer than 'config_<mm>_<YY>.py'
    cwd = os.getcwd()
    config_path = os.path.join(cwd, 'Config')
    if config_path not in sys.path:
        sys.path.insert(0, config_path)

    working_days = {}
    csv_file = os.path.join(config_path, f'config_{month}_{year}.csv')
    if os.path.isfile(csv_file):
        working_dates_and_types = config_csv_processing(month, year)
        for date, type_ in working_dates_and_types.items():
            working_days.update({date: getattr(DailyEarnTypes, type_)})
    else:
        monthly_config_module = importlib.import_module(f'config_{month}_{year}')
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
        #  NaN in 'Extra to planned' column can force integer in 'Date' columns to become floating
        # print(f'{date}: {earn_daily.type:19} -> {earn_daily.daily_salary():.2f}')
        # fp.write(f'{date}: {earn_daily.type:19} -> {earn_daily.daily_salary():.2f}\n')
        salary += earn_daily.daily_salary()
        day_of_month_candidate = date.split('.')[0]
        if day_of_month not in day_of_month_candidate:
            days += 1
            day_of_month = day_of_month_candidate
        else:
            day_of_month = day_of_month_candidate + '+'
        print(f'{day_of_month}: {earn_daily.type:19} -> {earn_daily.daily_salary():.2f}')
        fp.write(f'{day_of_month}: {earn_daily.type:19} -> {earn_daily.daily_salary():.2f}\n')

        all_hours += earn_daily.get_hours_num()
        daily_extra_hours = earn_daily.get_extra_hours()
        for key, val in daily_extra_hours.items():
            extra_hours[key] += daily_extra_hours[key]

    print('\n' + '=' * 10 + ' Summary ' + '=' * 10)
    fp.write('\n' + '=' * 10 + ' Summary ' + '=' * 10 + '\n')

    print(f'Salary month = {salary:.2f}')
    fp.write(f'Salary month = {salary:.2f}\n')

    print(f'Working days  = {days}')
    fp.write(f'Working days  = {days}\n')

    print(f'All hours = {all_hours}')
    fp.write(f'All hours = {all_hours}\n')

    regular_hours_num = all_hours - sum(extra_hours.values())
    detailed_hours = {'100%': regular_hours_num}
    verbal_extra_hours = {key.split('_')[1]+'%': val for (key, val) in extra_hours.items()}  # human view
    detailed_hours.update(verbal_extra_hours)
    print(f'Detailed hours = {detailed_hours}')
    fp.write(f'Detailed hours = {detailed_hours}\n')
    fp.close()
