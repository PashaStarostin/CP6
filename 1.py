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


a = [int(x) for x in input().split()]

m = f(a)

print(rep(a, m))