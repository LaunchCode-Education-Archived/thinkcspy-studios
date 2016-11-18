def bubble_sort(lst):
""" Sorts a list using bubble sort.
Does not alter the original list but returns a sorted version of it.
"""

    is_sorted = False
    while is_sorted == False:
        nswaps = 0
        for i in range(0, len(lst) - 1):
            a = lst[i]
            b = lst[i+1]
            if a > b:
                lst[i] = b
                lst[i+1] = a
                nswaps = nswaps + 1
        if nswaps == 0:
            is_sorted = True
    return lst
