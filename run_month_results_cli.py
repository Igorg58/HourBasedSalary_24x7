import argparse
from datetime import datetime
from month_results import month_results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--month', help='Month (MM)', type=str, required=False, default=None)
    parser.add_argument('-Y', '--year', help='Year (YY)', type=str, required=False, default=None)
    args = parser.parse_args()

    if args.month is None or args.year is None:
        now = datetime.now()
        month = str(now.month)
        if len(month) == 1:
            month = '0' + month
        year = str(now.year)[-2:]

    else:
        month = args.month
        year = args.year
        if len(month) == 1:
            month = '0' + month
        if len(year) == 4:
            year = year[-2:]

    month_results(month, year)


if __name__ == '__main__':
    main()