def jok(a,b):
    for i in a:
        c = b - i
        if c in a and i != c:
            return a.index(c), a.index(i)