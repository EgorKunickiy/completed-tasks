def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        j = i
        while j >= 0 and arr[j-1] < arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

def heap_sort(arr: list) -> list:

    def reshuffle(left: int, right: int):
        if arr[right] > arr[left]:
            arr[right], arr[left] = arr[left], arr[right]

    def value_check(size: int):
        for ind in range(size, 0, -1):
            if ind % 2 == 0:
                reshuffle((ind - 2) // 2, ind)
            else:
                reshuffle((ind - 1) // 2, ind)

    for i in range(len(arr)-1, 0, -1):
        value_check(i)
        arr[i], arr[0] = arr[0], arr[i]
    return arr

def selection_sort(arr: list) -> list:
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr.pop(arr.index(min(arr))))
    return new_arr

def fast_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    else:
        sr = arr[0]
        arr1 = []
        arr2 = []
        for i in arr:
            if i < sr:
                arr1.append(i)
            elif i > sr:
                arr2.append(i)
        return fast_sort(arr1) + [sr] + fast_sort(arr2)

if __name__ == "__main__":
    print(selection_sort([4, 3, 5, 6, 1, 4]))
    print(fast_sort([2, 4, 7, 6, 34, 5, 42, 555]))
    print(heap_sort([2, 4, 7, 6, 34, 5, 42, 555]))
    print(insertion_sort([4, 3, 5, 6, 1, 4]))