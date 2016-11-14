from test import testEqual

def remove_char(a_str, a_char):

    new_str = ''

    for idx in range(len(a_str)):
        if a_str[idx] != a_char:
            new_str = new_str + a_str[idx]

    return new_str

testEqual(remove_char('aardvark', 'a'), 'rdvrk')
testEqual(remove_char('aardvark', 'k'), 'aardvar')
testEqual(remove_char('asdf', 'z'), 'asdf')
testEqual(remove_char('', 'a'), '')
