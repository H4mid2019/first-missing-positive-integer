def solution2(a):
    b = [x for x in a if x > 0]
    if len(b) == 0:
        return '1'
    b.sort()
    b = list(set(b))
    c = 1
    for i in b:
        if i != c:
            break
        c += 1
    return c




""" 
This method is much faster than pervious method
"""