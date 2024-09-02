num=int(input("enter the numberr"))


def is_harshad(n):
    return n % sum(int(digit) for digit in str(n)) == 0


print(f"{num} is Harshad: {is_harshad(num)}")
