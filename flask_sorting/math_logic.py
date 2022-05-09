from sorting_methods import insertion_sort, selection_sort, heap_sort, quick_sort
from timeit import default_timer as timer
from parser import parse

LIST_OF_SORTING = {
    "selection sort": selection_sort,
    "insertion sort": insertion_sort,
    "fast sort": quick_sort,
    "heap sort": heap_sort
}


def get_sort(data: list, func: str) -> dict:
    final_dict = dict()
    for sequence in data:
        start = timer()
        if func == 'fast sort':
            result = LIST_OF_SORTING[func](sequence.copy(), 0, len(sequence)-1)
        else:
            result = LIST_OF_SORTING[func](sequence.copy())
        end = timer()
        final_dict[str(result)] = str(end-start)

    return final_dict


if __name__ == "__main__":
    d = [[3, 2, 14, 5, 78, 9, 8765, 3], [5, 43, 2, 345, 6, 789, 6, 52]]
    print(get_sort(d, 'heap sort'))
    print(d)
    print(id(d))
