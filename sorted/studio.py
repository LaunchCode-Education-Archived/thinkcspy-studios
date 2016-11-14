def is_sorted(string):
    """Returns True if string is sorted from least to greatest
       False otherwise.
    """

    for idx in range(len(string)-1):
        if string[idx] > string[idx + 1]:
            return False

    return True
