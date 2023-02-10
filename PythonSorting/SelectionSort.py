# https://www.geeksforgeeks.org/selection-sort/
from typing import List


def selection_sort(input_list: List) -> List:
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] > input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list

print(selection_sort([7, 3, 2, 5, 8, 7]))
