# https://www.geeksforgeeks.org/insertion-sort/
from typing import List


def insertion_sort(input_list: List) -> List:
    for i in range(1, len(input_list)):
        key = input_list[i]
        j = i - 1
        while j >= 0 and input_list[j] > key:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = key
    return input_list


print(insertion_sort([7, 3, 2, 5, 8, 7]))
