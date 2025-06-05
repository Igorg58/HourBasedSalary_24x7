import os.path
import pandas as pd
from datetime import date
from daily_earning import DailyEarnTypes


def config_csv_processing(month: str, year: str):
    # Build config csv filename
    filename = f'config_{month}_{year}.csv'
    path = os.path.join('Config', filename)  # TODO: check exist

    working_dates_and_types = {}

    df = pd.read_csv(path)
    print(df)  # debug
    for index, row in df.iterrows():
        dt = date(int('20' + year), int(month), int(row['Date']))
        week_day = dt.weekday()
        if week_day == 5:
            day_of_week = 'saturday'  # TODO: check 'Eve Holiday' and 'Holiday'
        elif week_day == 4:
            day_of_week = 'friday'  # TODO: check 'Eve Holiday' and 'Holiday'
        else:
            day_of_week = 'regular' # TODO: regular in DailyEarnTypes move to the beginning

        hours_num = int(row['End']) - int(row['Start'])
        if hours_num < 0:
            hours_num += 24

        part_of_day = ''
        if int(row['Start']) == 7:
            part_of_day = 'morning'
        elif int(row['Start']) == 15:
            part_of_day = 'evening'
        elif int(row['Start']) in [19, 23, 24]:
            part_of_day = 'night'

        # Changes because 'Eve Holiday' and 'Holiday'
        if int(row['Holiday']) == 1 and part_of_day == 'morning':
            day_of_week = 'saturday'
        if int(row['Eve Holiday']) == 1 and part_of_day == 'night':
            day_of_week = 'friday'

        day_earn_type = f'{day_of_week}_{part_of_day}_{hours_num}'
        attr = getattr(DailyEarnTypes, day_earn_type, None)
        if attr is None:
            print(f'Error in {filename} row:{row['Date']}.{month}')
            continue

        working_dates_and_types.update({f'{row['Date']}.{month}': day_earn_type})

        # Extra to was planned
        nan_in_row = row.isna()
        # print(type(nan_in_row), len(nan_in_row), nan_in_row['Extra to planned'])
        if not nan_in_row['Extra to planned']:
            working_dates_and_types.update({f'{row['Date']}.{month}+': row['Extra to planned']})

    return working_dates_and_types


def main():
    month = '06'  # '04'
    year = '25'
    working_dates_and_types = config_csv_processing(month, year)
    # print(working_dates_and_types)
    for d_m, earn_type in working_dates_and_types.items():
        print(f'{d_m}: {earn_type}')


if __name__ == '__main__':
    main()
