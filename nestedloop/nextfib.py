num=int(input("enter the number : "))
num1,num2=0,1
num3=1
while(num3<=num):
    num3=num1+num2
    num1=num2
    num2=num3
print(f"the next fibonaci number is {num3}")
   