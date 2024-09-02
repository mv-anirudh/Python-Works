years = [1000, 1002, 2000, 2004, 2001, 2008, 2016, 2028, 1800]
#print leap years
for year in years:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year)

        