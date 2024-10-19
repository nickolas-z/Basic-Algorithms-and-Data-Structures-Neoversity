import timeit

def binary_search_with_upper_bound(arr, target):
    low, high = 0, len(arr) - 1
    # Потрібно повернути кількість зроблених ітерацій (в прикладі це було забрано :) )
    iterations = 0
    upper_bound = arr[-1]  # Початкове значення - максимальний елемент масиву

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            # Не забуваємо за випадок, якщо шукане рівне тому що перевіряємо щоб не робити більше ітерацій ніж потрібно
            return arr[mid]

    return upper_bound

def exponential_search(arr, x):
    n = len(arr)
    if n == 0:
        return -1

    # Find range for binary search by repeatedly doubling i
    i = 1
    while i < n and arr[i] < x:
        i *= 2

    # Perform binary search on the range [i/2, min(i, n-1)]
    left = i // 2
    right = min(i, n-1)
 
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
 
    return -1
 
     
arr = list(range(1000000))
x = 2000

# Timeit for exponential_search
exponential_time = timeit.timeit(lambda: exponential_search(arr, x), number=1000)

# Timeit for binary_search_with_upper_bound
binary_time = timeit.timeit(lambda: binary_search_with_upper_bound(arr, x), number=1000)

print("Exponential search execution time:", exponential_time)
print("Binary search with upper bound execution time:", binary_time)