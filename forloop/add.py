num=int(input("enter a number "))
sum=0
digit=0
for i in range(1,num+1):
    digit=(digit*10+num)
    sum+=digit
    
    print(digit)
print(f"the sum is {sum}")
    
