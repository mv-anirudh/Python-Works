def even_position_elements(arr):
    return [arr[i] for i in range(len(arr)) if i % 2 == 0]

arr = [1, 2, 3, 4, 5, 6]
print(f"Elements on even positions: {even_position_elements(arr)}")
