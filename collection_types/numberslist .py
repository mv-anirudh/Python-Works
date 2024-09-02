numbers=[10,11,12,34,43,54,19,78,42]
number_count=len(numbers)
print(len(numbers))


#print even numbers
for i in range(0,number_count):
    if numbers[i]%2==0:
        print(numbers[i])

#print total of numbers
total=0
for i in range (0,number_count):
    total=total+numbers[i]
print(f"total is {total}")
    
#print total of odd_numbers
odd_total=0
for i in range (0,number_count):
    if numbers[i]%2!=0:
        odd_total=odd_total+numbers[i]
print(f"odd total is {odd_total}")
    