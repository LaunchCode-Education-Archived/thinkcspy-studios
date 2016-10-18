# Sorts a list using bubble sort.
# Does not alter the original list but returns a sorted version of it.
def bubble_sort(lst):
    # TODO your code here



from test import testEqual
testEqual(bubble_sort([0]), [0])  # Sorts a single element, returns same list
testEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Sorted list is the same
testEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
testEqual(bubble_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
