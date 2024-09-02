def fib(num):
    if num == 0 or num == 1:
        return True
    
    num1, num2 = 0, 1
    while num2 <= num:
        if num == num2:
            return True
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        
    return False
        
print(fib(3))  
