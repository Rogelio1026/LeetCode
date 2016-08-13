def Fibonacci_sequence(number):
    """

    :param number: int
    :return: list
    """
    a = 1
    b = 1
    list_1 = [a,b]
    for i in range(number-2):
        list_1.append(a+b)
        c = a + b
        a = b
        b = c
    if number > 1:
        return list_1
    elif number == 1:
        return [1]
    else:
        return 'Wrong number'

if __name__ == '__main__':
    assert (Fibonacci_sequence(1) == [1])
    assert (Fibonacci_sequence(2) == [1,1])
    assert (Fibonacci_sequence(3) == [1,1,2])
    assert (Fibonacci_sequence(5) == [1,1,2,3,5])
    assert (Fibonacci_sequence(0) == 'Wrong number')