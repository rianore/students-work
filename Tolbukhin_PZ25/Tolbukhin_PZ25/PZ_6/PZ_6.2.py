#Дан список размера N. Найти количество участков,
# на которых его элементы мнотонно убывают.
def count_decreasing_subarrays(arr):
    n = len(arr)
    count = 0
    i = 0
    while i < n - 1:
        while i < n - 1 and arr[i] >= arr[i + 1]:
            i += 1
        if i < n - 1:
            count += 1
        i += 1
    return count

arr = [6, 5, 4, 8, 9, 7, 3, 2]
print(count_decreasing_subarrays(arr))