from test import testEqual

def remove_char(a_str, a_char):

    new_str = ''

    for this_char in a_str:
        if this_char != a_char:
            new_str = new_str + this_char

    return new_str

testEqual(remove_char('aardvark', 'a'), 'rdvrk')
testEqual(remove_char('aardvark', 'k'), 'aardvar')
testEqual(remove_char('asdf', 'z'), 'asdf')
testEqual(remove_char('', 'a'), '')
