num=int(input("enter a number "))
sum=0
original_num = num
digit_count=len(str(num))
while(num!=0):
       digit=num%10
       exponent=digit**digit_count
       sum+=exponent
       num=num//10
if sum==original_num:
       print(f"the number {original_num} is a amstrong number ")
else:
       print(f"number {original_num}  is not amstrong ")
    