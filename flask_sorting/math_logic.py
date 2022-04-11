from sorting_methods import insertion_sort, selection_sort, heap_sort, fast_sort
from timeit import default_timer as timer
from parser import parse

LIST_OF_SORTING = {
    "selection sort": selection_sort,
    "insertion sort": insertion_sort,
    "fast sort": fast_sort,
    "heap sort": heap_sort
}


def get_sort(data: dict, func: str) -> dict:
    final_dict = dict()
    list_seq = parse(data)
    for sequence in list_seq:
        start = timer()
        result = LIST_OF_SORTING[func](sequence)
        end = timer()
        final_dict[str(end-start)] = result

    return final_dict
