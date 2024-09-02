expenses=[1200,13000,14000,15000,21000,22000,13000]
total=0

#find count of objects in expenses
print(len(expenses))
expense_cont=(len(expenses))
#print all expenses
for i in range(0,expense_cont):
    print(expenses[i])

#print expenses>15000
# print([x for x in expenses if x>15000]
for i in range(0,expense_cont):
    if expenses[i]>15000:
        print(expenses[i])

#print total expense
# print(sum(expenses))
for i in range(0,expense_cont):
    total=total+expenses[i]
print(f"total sum is {total}")


#avg expense
avg=total/expense_cont
print(f"avg expense is {avg}")

