lst_of_bools = [False, False, False]

def any(lst):
    """Return True if any item in the list is true, false otherwise."""
    for x in lst:
        if x == True: # Could just be x.
            return True
    return False

print(any(lst_of_bools))
    
