########## EXERCISE 0 ##########

# in a list of numbers, print every ith number
def print_every(i, nums):
    counter = 0
    for i in nums:
        if counter % i == 0:
            print(i)
        counter += 1

print_every(3, [4, 7, 2, 8, 1, 0, 9, 6])
# should print 4, then print 8, then print 9



########## EXERCISE 1 ##########

# return True if every member of the group is at least 70, otherwise return False
def check_group(ages):
    for age in ages:
        if age < 70:
            return False
        else:
            return True


from test import testEqual

# this group should not be allowed inside the bar
group = [78, 71, 25, 84]
testEqual(check_group(group), False)

# this group should also not be allowed inside the bar
group2 = [ 2, 99 ]
testEqual(check_group(group2), False)

# this loner is allowed
group3 = [ 99 ]
testEqual(check_group(group3), True)



########## EXERCISE 2 ##########

def password_checker(password):
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

pw2 = "puzzlesr4fun"
print(password_checker(pw2))
# should print True

