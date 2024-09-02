# num=int(input("enter your string "))
# result=0
# orginal_num=num

# while(num!=0):
#  digit=num %10
#  result=result*10+digit
#  num=num//10
# if result==orginal_num:
#  print(f"the number {orginal_num} is palindrome")
# else:
#  print(f"the number {orginal_num} is not  palindrome")
strg=int(input("enter the word "))
string=str(strg)
string=string[::-1]
if string==string[::-1]:
    print("palindrome")
else:
    print("not palindrime")

 




