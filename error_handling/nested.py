num1=int(input("enter the number: "))
num2=int(input("enter the number "))

try:
    print(num1/num2)
except Exception as e:
    num2=int(input("enter the number"))
    result=num1/num2
    print(result)
    
finally: #this block will execute even if error occured
    print("file opaeration")
    print("db commit")
    