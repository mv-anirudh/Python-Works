height=int(input("enter your height : "))
weight=int(input("enter your weight : "))

height_in_m=height/100


bmi=weight/height_in_m**2

print(f"your bmi is {bmi}")
