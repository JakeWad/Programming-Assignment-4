def add(x):
    def inner(y):
        nonlocal x
        x += y
        return inner
    inner.__call__ = inner
    inner.__str__ = lambda self: str(x)
    return inner
