num=int(input("enter the number : "))
num1,num2=0,1
print("fibonacci series is ",num1,num2,end=" ")
for i in range(0,num):  
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=" ")