

def recursive(unordered_list):
    recursive_sort(unordered_list, 0, len(unordered_list))
    return unordered_list


def recursive_sort(local_list, start, end):
    if end - start <= 1:
        return

    middle = start + int((end - start) / 2)

    recursive_sort(local_list, start, middle)
    recursive_sort(local_list, middle, end)
    merge(local_list, start, middle, end)


def merge(local_list, start, middle, end):
    merge = [None] * (end - start)
    left = 0
    right = 0
    i = 0
    while left < middle - start and right < end - middle:

        if local_list[start + left] < local_list[middle + right]:
            merge[i] = local_list[start + left]
            left += 1
        else:
            merge[i] = local_list[middle + right]
            right += 1
        i += 1

    while right < end - middle:
        merge[i] = local_list[middle + right]
        i += 1
        right += 1

    while left < middle - start:
        merge[i] = local_list[start + left]
        i += 1
        left += 1

    local_list = copy_list(merge, 0, local_list, start)


def copy_list(source_list, source_start_index, destination_list, destination_start_index):
    source_splice = source_list[source_start_index:len(source_list)]
    for num in source_splice:
        destination_list[destination_start_index] = num
        destination_start_index += 1
    return destination_list


def sort(numbers):
    return_numbers = recursive(numbers)
    return return_numbers
