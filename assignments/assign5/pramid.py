# print a * pyramid 
for row in range(1,5):
    print(" "*(5-row),end="")
    for col in range(1,row):
     print("*",end=" ")
    print()