year=int(input("enter year: "))

if (year%4==0 and year%100!=0)or (year%400==0):
    print(f"the year {year} is leap year")
else:
    print("not leap year")