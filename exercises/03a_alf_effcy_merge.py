# Different algs for merge sort:
#  First method combines the whole divide/conquer/combine process in one
#  one function that calls itself recursively until sort is completed.
#  Second method breaks this process down into separate functions,
#  merge_sort_v2 and merge_v2. merge_sort splits given list and recursively sorts them.
#  If the lists are singletons, you've got the base case. Another function,
#  merge_v2 is used for merging the sorted sublists and returning the resulting
#  sorted list.

# METHOD ONE:

count = 0


def merge_sort(sort_list):
    if len(sort_list) > 1:
        mid = len(sort_list) // 2
        left_half = sort_list[:mid]
        right_half = sort_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sort_list[k] = left_half[i]
                i = i + 1
            else:
                sort_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            sort_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            sort_list[k] = right_half[j]
            j = j + 1
            k = k + 1

    global count
    count += 1
    if len(sort_list) == len(lst):
        # print("Sorted: ", sort_list)
        print("Number of comparisons, method one: ", count)
        return lst


# Driver code for testing
lst = [7, 9393, 4, 23, 1, 88, 34, 29, 17, 52]
sorted_lst = merge_sort(lst)
print('Sorted with method one: ', sorted_lst)

#####################################################################


# METHOD TWO:

def merge_V2(sort_list, p, q, r):
    # Initialize vars for length of the first and second sublists
    n1 = q - p + 1
    n2 = r - q

    # Create temporary arrays
    l = [0] * n1
    r = [0] * n2

    # Copy arr[1..q] to temp array l[]
    for i in range(0, n1):
        l[i] = sort_list[p + i]

    # Copy arr[q+1..r] to r[]
    for j in range(0, n2):
        r[j] = sort_list[q + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = p  # Initial index of merged subarray

    while i < n1 and j < n2:
        if l[i] <= r[j]:
            sort_list[k] = l[i]
            i += 1
        else:
            sort_list[k] = r[j]
            j += 1
        k += 1

    # Copy the remaining elements of l[], if there
    # are any
    while i < n1:
        sort_list[k] = l[i]
        i += 1
        k += 1

    # Copy the remaining elements of r[], if there
    # are any
    while j < n2:
        sort_list[k] = r[j]
        j += 1
        k += 1


def merge_sort_V2(sort_list, p, r):
    if p < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = int((p + (r - 1)) / 2)
        # Sort first and second halves
        merge_sort_V2(sort_list, p, m)
        merge_sort_V2(sort_list, m + 1, r)
        merge_V2(sort_list, p, m, r)


# Driver code for testing
lst2 = [12, 11, 13, 5, 6, 7]
n = len(lst2)
merge_sort_V2(lst2, 0, n - 1)
print("Sorted with method two: ", lst2)

