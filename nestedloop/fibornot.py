num = int(input("Enter your number: "))


if num == 0 or num == 1:
    isFibonacci = True
else:
    num1, num2 = 0, 1
    isFibonacci = False
    
    while num2 <= num:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        if num == num2:
            isFibonacci = True
            break

if isFibonacci:
    print("The number is Fibonacci")
else:
    print("The number is not Fibonacci")
