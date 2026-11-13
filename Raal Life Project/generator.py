# Build a Number Pattern Generator

def number_pattern(n):

    if not isinstance(n, int) or isinstance(n, bool):
        return 'Argument must be an integer value.'

    if n < 1:
        return 'Argument must be integer greater than 0.'

    return " ".join(str(n) for n in range(1, n + 1))

def number_pattern1(n1):

    if not isinstance(n1, int) or isinstance(n1, bool):
        return 'Argument must be an integer value.'

    if n1 < 1:
        return 'Argument must be integer greater than 0.'

    return " ".join(str(n1) for n1 in range(10, n1 + 10))

print(number_pattern(4))
print(number_pattern(int))
print(number_pattern(0))
print(number_pattern(12))
print(number_pattern1(50))

