

def solution(a):
    a.sort()
    a = set(a)
    a = list(a)
    c = 0
    x = 0
    for i in enumerate(a):
        c += 1
        if i[1] > 0:
            if i[0]+1 != i[1] :
                x = i[0]+1
        elif i[1] < 0:
            pass
    if c == len(a) and x == 0:
        return 1
    else:
        return x
