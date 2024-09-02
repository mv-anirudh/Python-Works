Str=input("enter the string")
lower=0
upper=0
for i in Str:
	if(i.isupper()):
			upper+=1
	else:
			lower+=1
print("The number of lowercase characters is:",lower)
print("The number of uppercase characters is:",upper)
