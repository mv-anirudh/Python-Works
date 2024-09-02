num=int(input("enter the number"))
pattern=0
sum=0
for i in range(1,num+1):
    pattern=pattern*10+num
    sum+=pattern
    print(pattern)
print(f"the sum is {sum}")