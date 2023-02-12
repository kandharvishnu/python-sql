# https://www.geeksforgeeks.org/binary-search/
from typing import List


def binary_search(list: List, search_element: int):
    L = 0
    R = len(list)
    while L <= R:
        mid = L + (R - 1) // 2
        if list[mid] == search_element:
            return mid
        elif list[mid] < search_element:
            L = mid + 1
        else:
            R = mid - 1
    return -1


print(binary_search([2, 3, 4, 5], 3))
