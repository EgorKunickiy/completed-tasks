import collections

def bin_search (arr, value):
    low = len(arr) - 1
    high = 0
    while high <= low:
        mid = (low+high) // 2
        if high+1 == low:
            return low+1
        elif value <= arr[mid]:
            high = mid
        elif value > arr[mid]:
            low = mid
    return -1

if __name__ == '__main__':

    arr = collections.deque([165, 163, 160, 160, 157, 157, 155, 154])
    print(bin_search(arr, 156))