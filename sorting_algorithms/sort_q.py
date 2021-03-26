
def partition(list_to_sort, left, right):
    pivot = list_to_sort[left]
    while True:
        while list_to_sort[left] < pivot:
            left += 1

        while list_to_sort[right] > pivot:
            right -= 1

        if left < right:
            temp = list_to_sort[right]
            list_to_sort[right] = list_to_sort[left]
            list_to_sort[left] = temp
        else:
            return right


def sort_algo(list_to_sort, left, right):
    if left < right:
        pivot = partition(list_to_sort, left, right)

        if pivot > 1:
            sort_algo(list_to_sort, left, pivot - 1)

        if pivot + 1 < right:
            sort_algo(list_to_sort, pivot + 1, right)


def sort(list_to_sort):
    sort_algo(list_to_sort, 0, len(list_to_sort) - 1)
    return list_to_sort
