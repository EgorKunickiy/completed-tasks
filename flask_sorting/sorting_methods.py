from timeit import default_timer as timer
import random


def insertion_sort(arr):

    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key
    return arr


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)
    return arr


def selection_sort(arr: list) -> list:
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr.pop(arr.index(min(arr))))

    return new_arr


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: list, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


if __name__ == "__main__":
    array = list(r(-100, 100) for r in [random.randint]*50)
    functions = [selection_sort, heap_sort, quick_sort, insertion_sort]
    for func in functions:
        if func == quick_sort:
            t = timer()
            print(func(array.copy(), 0, len(array)-1) == sorted(array))
            result = timer() - t
            print(f'{func.__name__}: {result * 1000}')
        else:
            t = timer()
            print(func(array.copy()) == sorted(array))
            result = timer() - t
            print(f'{func.__name__}: {result * 1000}')
