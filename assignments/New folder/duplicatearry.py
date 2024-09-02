def find_duplicates(arr):
    duplicates = set([x for x in arr if arr.count(x) > 1])
    return list(duplicates)

arr = [1, 2, 3, 2, 4, 5, 6, 5]
print(f"Duplicate elements: {find_duplicates(arr)}")
