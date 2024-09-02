def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

num1=float(input("enter the number : "))
num2=float(input("enter the number : "))

print("Please select operation -\n" 
        "1. Add\n" 
        "2. Subtract\n" 
        "3. Multiply\n" 
        "4. Divide\n")

select=int(input("select operation from 1:2:3:4 : "))
if select==1:
    print(num1 ,"+", num2 ,"=", add(num1,num2))
elif select==2:
    print(num1 ,"-", num2 ,"=", sub(num1,num2))
elif select==3:
    print(num1 ,"+", num2 ,"=", mul(num1,num2))
elif select==4:
    print(num1 ,"+", num2 ,"=", div(num1,num2))
else:
    print("invalid choice")
    

   
    
    

