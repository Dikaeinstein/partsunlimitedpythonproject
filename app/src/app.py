def my_sum(param1, param2):
    """Calculates the sum of two numbers."""
    result = None
    try:
        result = param1 + param2
    except TypeError:
        result = 'invalid arguments'

    return result


if __name__ == '__main__':
    print(my_sum('1', 1))
