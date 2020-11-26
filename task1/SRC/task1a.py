#в python нет перегрузки функций
#здесь дополнительная часть задания

def dectobase(i, base):
    a = len(base)
    res = ''
    while i >= a:
        res += str(base[i % a])
        i //= a
    res += str(base[i])
    return res[::-1]


def itoBase(nb, baseSrc, baseDst):
    s = len(baseSrc)
    d = len(nb)
    dec = 0
    for i in range(d):
        dec += baseSrc.find(nb[i]) * s**(d - i - 1)
    return dectobase(dec, baseDst)


nb = str(input())
baseSrc = str(input())
baseDst = str(input())
print(itoBase())






