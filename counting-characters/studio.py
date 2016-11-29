test_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

char_count = {}

for c in test_string:

    if not char_count.get(c):
        char_count[c] = 1
    else:
        char_count[c] += 1

for (c, count) in char_count.items():
    print(c + ":", count)
