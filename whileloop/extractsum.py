num=int(input("enter a number "))
sum =0
while(num!=0):
      digit=num%10
      print(f"the digits are {digit}")
      sum+=digit
      num=num//10
print(f"the sum of digits is {sum}")

