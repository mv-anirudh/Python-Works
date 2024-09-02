num =int(input("enter the number"))


def is_disarium(n):
    num_str = str(n)
    length = len(num_str)
    sum = 0
    for i in range(length):
        sum += int(num_str[i]) ** (i + 1)
    return sum == n

print(f"{num} is Disarium: {is_disarium(num)}")
