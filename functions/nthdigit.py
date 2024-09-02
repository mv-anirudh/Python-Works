def nth_digit_max(n1,n2):
    return n1 if n1%10 >n2%10 else n2
    
#         last_num1= n1%10
#         last_num2= n2%10
#         if last_num1>last_num2:
#             return n1
#         else:
#               return n2
print(nth_digit_max(19,18))

