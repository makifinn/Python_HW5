a = int(input('введите число "a": '))
b = int(input('введите число "b": '))

def rec_sum(a: int, b: int):
    if a < b:
        a, b = b, a
    if b == 1:
        return a
    return a + rec_sum(a, b - 1)

print(rec_sum(a, b))