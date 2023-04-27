a = int(input('введите число "a": '))
b = int(input('введите число "b": '))

def exponentiate(a: int, b: int):
    if b == 1:
        return a
    return a * exponentiate(a, b - 1)

print(exponentiate(a, b))