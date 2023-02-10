# https://www.geeksforgeeks.org/bubble-sort/
from typing import List


def bubble_sort(input_list: List) -> List:
    for i in range(len(input_list)):
        for j in range(len(input_list) - 1 - i):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return input_list


print(bubble_sort([7, 3, 2, 5, 8, 7]))
