def hcf(x, y):
    while y:
        x, y = y, x % y
    return x

num1 = int(input("enter the numberr"))
num2 = int(input("enter the numberr"))

print(f"The HCF of {num1} and {num2} is {hcf(num1, num2)}")
