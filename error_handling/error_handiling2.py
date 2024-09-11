num1=int(input("enter the number"))

num2=input("enter the number ")

try:
    result=num1+num2 # type: ignore
    print(result)
except Exception as e:
    print("invalid input",e)
    result=(num1)+int(num2)
    
    
finally:
    print(result)
    print("db commit")
    

