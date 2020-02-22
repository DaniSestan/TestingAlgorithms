from __future__ import division
import sys


SENTINEL = sys.maxsize


def merge(sort_list, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left_sublist = [None for t in range(n1 + 1)]
    right_sublist = [None for t in range(n2 + 1)]

    for i in range(n1):
        left_sublist[i] = sort_list[p + i - 1]

    for j in range(n2):
        right_sublist[j] = sort_list[q + j]

    left_sublist[n1] = SENTINEL

    right_sublist[n2] = SENTINEL

    i = 0
    j = 0
    for k in range(p - 1, r):
        if left_sublist[i] <= right_sublist[j]:
            sort_list[k] = left_sublist[i]
            i = i + 1
        else:
            sort_list[k] = right_sublist[j]
            j = j + 1


def mergeSort(sort_list, p, r):
    if p < r:
        q = int((p + r) / 2)
        mergeSort(sort_list, p, q)
        mergeSort(sort_list, q + 1, r)

        merge(sort_list, p, q, r)


# Driver code for testing
lst = [5, 2, 4, 7, 1, 3, 2, 6]
mergeSort(lst, 1, len(lst))
print(lst)