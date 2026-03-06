def bubble_sort(lst):
    """
    Сортировка пузырьком.
    Не изменяет исходный список.
    """
    arr = list(lst)
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


def merge_sort(lst):
    """
    Сортировка слиянием.
    Не изменяет исходный список.
    """
    arr = list(lst)

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def binary_search(lst, target):
    """
    Бинарный поиск в отсортированном списке.
    Возвращает индекс элемента или -1.
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        if lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def find_kth_largest(lst, k):
    """
    Возвращает k-й наибольший элемент.
    k считается с 1: k=1 -> самый большой элемент.
    """
    if not lst:
        raise ValueError("Список пуст")
    if k < 1 or k > len(lst):
        raise ValueError("Некорректное значение k")

    sorted_desc = sorted(lst, reverse=True)
    return sorted_desc[k - 1]
