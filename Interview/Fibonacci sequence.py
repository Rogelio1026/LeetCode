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
    return list_1

if __name__ == '__main__':
    print(Fibonacci_sequence(3))