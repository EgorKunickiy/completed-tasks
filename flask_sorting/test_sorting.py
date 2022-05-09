import numpy as np
import random
import unittest
from sorting_methods import selection_sort, heap_sort, quick_sort, insertion_sort

list1 = list(r(-100, 100) for r in [random.randint]*100)
list2 = list(np.random.randint(-1000, 1000, 1000))
list3 = list(np.random.randint(-10000, 10000, 10000))
list4 = list(np.random.randint(-100000, 100000, 100000))


class TestSort(unittest.TestCase):
    def test_quick_sort(self):
        assert quick_sort(list1.copy(), 0, len(list1)-1) == sorted(list1)
        assert quick_sort(list2.copy(), 0, len(list2)-1) == sorted(list2)
        assert quick_sort(list3.copy(), 0, len(list3)-1) == sorted(list3)
        assert quick_sort(list4.copy(), 0, len(list4)-1) == sorted(list4)

    def test_selection_sort(self):
        assert selection_sort(list1.copy()) == sorted(list1)
        assert selection_sort(list2.copy()) == sorted(list2)
        assert selection_sort(list3.copy()) == sorted(list3)
        # assert selection_sort(list4.copy()) == sorted(list4)

    def test_heap_sort(self):
        assert heap_sort(list1.copy()) == sorted(list1)
        assert heap_sort(list2.copy()) == sorted(list2)
        assert heap_sort(list3.copy()) == sorted(list3)
        assert heap_sort(list4.copy()) == sorted(list4)

    def test_insertion_sort(self):
        assert insertion_sort(list1.copy()) == sorted(list1)
        assert insertion_sort(list2.copy()) == sorted(list2)
        assert insertion_sort(list3.copy()) == sorted(list3)
        # assert insertion_sort(list4.copy()) == sorted(list4)


if __name__ == "__main__":
    unittest.main()
