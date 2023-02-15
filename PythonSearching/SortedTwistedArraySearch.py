# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

def search(input_list, key, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if input_list[mid] == key:
        return mid
    if input_list[left] <= input_list[mid]:
        if input_list[left] <= key <= input_list[mid]:
            return search(input_list, key, left, mid - 1)
        return search(input_list, key, mid + 1, right)
    if input_list[mid] <= key <= input_list[right]:
        return search(input_list, key, mid + 1, right)
    return search(input_list, key, left, mid - 1)


input_list = [4, 5, 6, 7, 9, 1, 2, 3]
print(search(input_list, 9, 0, len(input_list) - 1))
