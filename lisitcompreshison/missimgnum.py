arr=[0,2,3,4]
n=len(arr)
sum_of_n=n*(n+1)/2

cur_sum=sum(arr)
for num in arr:
    if sum_of_n==cur_sum:
        print("no missing function")
    else:
        mising_num=sum_of_n-cur_sum
print(mising_num)
