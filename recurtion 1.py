""" Максимальное значение с РОР
         в одну строку"""


def max(ar):
    if len(ar) == 2:
        return ar[0] if ar[0] > ar[1] else ar[1]
    x = ar.pop(0)
    y = ar[0]
    return (max(ar)) if (max(ar)) > x else x if x > y else x


print(max([96, 2, 31, 184]))
