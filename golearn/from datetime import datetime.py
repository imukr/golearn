from datetime import date


def get_days_in_month(month, year):
    start = date(year, month, 1)
    stop = date(year, month+1,1)
    u = stop - start
    return print(u.days)

get_days_in_month(3, 2021)
    