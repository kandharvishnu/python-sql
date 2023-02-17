# https://www.baeldung.com/java-kth-largest-element#:~:text=If%20we%20sort%20the%20array,length(Array)%20%E2%80%93%20k.
import heapq


def kth_largest_element(arr, K):
    N = len(arr)
    pqL = arr[0:K]
    heapq.heapify(pqL)
    print(pqL)
    for i in range(K, N):
        if arr[i] > pqL[0]:
            heapq.heapreplace(pqL, arr[i])
    pqS = arr[0:K]
    heapq._heapify_max(pqS)
    for i in range(K, N):
        if arr[i] < pqS[0]:
            heapq._heapify_max(pqS)

    return pqL[0], pqS[0]


print(kth_largest_element([8, 9, 1, 2, 3, 4, 5, 6, 7], 2))
arr = [12, 3, 5, 7, 19, 20]
K = 2
k = len(arr) + 1 - 4
s = set(arr)
for i in s:
    if K == 1:
        print(i)
    if k == 1:
        print(i)
    K -= 1
    k -= 1
