Calculate monthly salary based on hour's rate and working hours, regular as well as extra and weekends.
According to Israel's Labor Law.

Run application from CLI:
    1. Goto to HourBaseSalary_24x7 directory 
        $ cd C:\Python Projects\HourBasedSalary_24x7
    2. If you want to get results for certain month and year, 
       run python script run_month_results_cli.py with parameters, like in the following example:
       $ python run_month_results_cli.py -m 04 -Y 25
            '-m', '--month', help='Month (MM)'
.           '-Y', '--year', help='Year (YY)'
        If you want to get results for current month, 
        run python script run_month_results_cli.py without parameters, like in the following example:
        $ python run_month_results_cli.py
