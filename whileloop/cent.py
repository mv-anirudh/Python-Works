#print all cent years 
start_year=1800
end_year=2024
while(start_year<=end_year):
    if start_year%100==0:
        print(start_year,end=" ")
    start_year+=1        