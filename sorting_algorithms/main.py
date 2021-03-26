from sort_q import sort as sort_q
from sort_m import sort as sort_m
from sort_i import sort as sort_i

some_list = [3, 8, 7, 5, 2, 1, 9, 6, 4]

sorted_list_from_m = sort_m(some_list)
sorted_list_from_q = sort_q(some_list)
sorted_list_from_i = sort_i(some_list)

print(f'Sort M Result: {sorted_list_from_m}')
print(f'Sort Q Result: {sorted_list_from_q}')
print(f'Sort I Result: {sorted_list_from_i}')
