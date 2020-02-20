# lst = [3, 2, 4, 5, 7, 7]
lst = [7, 2, 3, 4, 5, 6, 7, 1, 2, 11, 2, 123, 4, 2, 4, 5, 333]
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
        print("Number of comparisons: ", count)


merge_sort(lst)
