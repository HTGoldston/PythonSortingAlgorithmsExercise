def sort_algo(list_to_sort, length):
    for i in range(length):
        j = i
        while j > 0:
            if list_to_sort[j - 1] > list_to_sort[j]:
                temp = list_to_sort[j - 1]
                list_to_sort[j - 1] = list_to_sort[j]
                list_to_sort[j] = temp
                j -= 1
            else:
                break
    return list_to_sort


def sort(list_to_sort):
    sorted_list = sort_algo(list_to_sort, len(list_to_sort))
    return sorted_list
