from datetime import datetime
from month_results import month_results


def main():
    current = input('Current month results?: Y/N \n')
    if current.lower() == 'y':
        now = datetime.now()
        month = str(now.month)
        if len(month) == 1:
            month = '0' + month
        year = str(now.year)[-2:]

    else:
        month = input('Enter month MM: \n')
        year = input('Enter year YY: \n')
        if len(month) == 1:
            month = '0' + month
        if len(year) == 4:
            year = year[-2:]

    month_results(month, year)


if __name__ == '__main__':
    main()