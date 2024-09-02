start_limit = int(input("enter the start limit "))
end_limit = int(input("enter the ending limit "))
for start_limit in range(start_limit,(end_limit+1)):
    if start_limit % 2 != 0:
        print(start_limit)
    start_limit += 1