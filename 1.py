def f(a):
    l = len(a)
    if l == 0:
        return "ошибка"
    maxim = -11111111111111111111
    for i in range(l):
        if a[i] > maxim:
            maxim = a[i]

    return maxim


def rep(a, maxim):
    k = 0
    for i in range(len(a)):
        if k == 0 and a[i] == maxim:
            k = 1
        elif k == 1:
            a[i] = 0

    return a


a = [1, 2, 3, 4, 5, 6, 7, 3, 4, 2, 1, 2, 3]

m = f(a)

print(rep(a, m))