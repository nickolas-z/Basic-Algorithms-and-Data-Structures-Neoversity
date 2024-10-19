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


if __name__ == '__main__':
    # Тестування функції
    arr = [1.1, 1.3, 2.5, 3.8, 4.6]
    print(binary_search_with_upper_bound(arr, 3.5))
    print(binary_search_with_upper_bound(arr, 4))
    print(binary_search_with_upper_bound(arr, 6.0))
    print(binary_search_with_upper_bound(arr, 2.5))
    print(binary_search_with_upper_bound(arr, 0)) 