# https://www.programiz.com/dsa/merge-sort

from typing import List


def merger_sort(input_list: List) -> List:
    if len(input_list) > 1:
        mid = len(input_list) // 2
        L = input_list[:mid]
        R = input_list[mid:]
        merger_sort(L)
        merger_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                input_list[k] = L[i]
                i += 1
            else:
                input_list[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            input_list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            input_list[k] = R[j]
            j += 1
            k += 1
    return input_list

print(merger_sort([7, 3, 2, 5, 8, 7]))
