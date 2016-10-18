########## EXERCISE 0 ##########

# in a list of numbers, print every ith number
def print_every(i, nums):
    counter = 0
    for n in nums:
        if counter % i == 0:
            print(n)
        counter += 1

print_every(3, [4, 7, 2, 8, 1, 0, 9, 6])
# should print 4, then print 8, then print 9





########## EXERCISE 2 ##########

def password_checker(password):
    """
    A valid password has no spaces, 
    and at least one non-alphabetical character
    """
    contains_non_alpha = False

    for char in password:
        if char == " ":
            return False
        else not char.isalpha():
            contains_non_alpha = True

    return contains_non_alpha

pw1 = "i <3 makonnen"
print(password_checker(pw1))
# should print False

pw2 = "puzzlesareforfun"
print(password_checker(pw2))
# should print False

pw2 = "puzzlesr4fun"
print(password_checker(pw2))
# should print True

