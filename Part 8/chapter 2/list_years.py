from datetime import date


def list_years(dates: list):
    dates = sorted(dates)
    new_List = []

    for  value in dates:
        new_List.append(value.year)
    
    return new_List


date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)
