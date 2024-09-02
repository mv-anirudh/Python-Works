arr = [10, 11, 12, 13, 14, 15, 16, 17]
odd_pos = [num  for num in arr if num%2!=0]
odd_pos.reverse()


left=1
length=len(arr)-1

right= length if length%2!=0 else length-1
while(left<right):
    (arr[left],arr[right])=(arr[right],arr[left])
    left=left+2
    right=right-2
print(arr)