num1=int(input("enter the first number "))
num2=int(input("enter the second number "))

for i in range(1,num1+1):
    if num1%i==0 and num2%i==0:
        fact1=i
print(f"gcd of {num1} and {num2} is {fact1}")

    



    
