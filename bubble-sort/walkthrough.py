from test import testEqual

def insert(sorted_list, num):

    new_idx = 0

    while new_idx < len(sorted_list) and num > sorted_list[new_idx]:
        new_idx += 1

    new_sorted_list = sorted_list[:new_idx]
    new_sorted_list.append(num)

    for item in sorted_list[new_idx:]:
        new_sorted_list.append(item)

    return new_sorted_list


testEqual(insert([2,3], 1), [1,2,3])
testEqual(insert([1,3], 2), [1,2,3])
testEqual(insert([1,2], 3), [1,2,3])
