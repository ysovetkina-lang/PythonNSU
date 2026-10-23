s = input()
c = s[0]
r = int(s[1])

if c == "a" or c == "c" or c == "e" or c == "g":    # если буква нечетная (a, c, e, g)
    if r % 2 == 1:
        print("черный")
    else:
        print("белый")
else:                                               # если буква четная (b, d, f, h)
    if r % 2 == 1:
        print("белый")
    else:
        print("черный")