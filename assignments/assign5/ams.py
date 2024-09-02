def is_amstrong(num):
    number=str(num)
    lent=len(number)
    expo=sum(int(digit) **lent for digit in number)
    return expo==num

print(is_amstrong(153))