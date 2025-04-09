def jok(a,b):
    for i in a:
        c = b - i
        if c in a:
            return a.index(c), a.index(i)