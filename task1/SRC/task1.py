def itoBase(i, base):
    a = len(base)
    res = ''
    while i >= a:
        res += str(base[i % a])
        i //= a
    res += str(base[i])
    return res[::-1]


i = int(input())
base = str(input())
print(itoBase(i, base))
