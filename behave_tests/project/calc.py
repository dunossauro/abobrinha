from numbers import Number


def add(x, y):
    if not isinstance(x, Number) or not isinstance(y, Number):
        return 'Insira um número'
    return x + y
