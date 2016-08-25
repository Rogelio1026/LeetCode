def Binary_search(number,list_1):
    """

    :param number: int
    :return: int
    """
    try:
        number == int(number)
    except ValueError:
        print("please enter an int")
        return 0
    finally:
        i = 0
        mid = len(list_1)/2
        if number > list_1[-1]:
            return len(list_1)-1
        elif number < list_1[0]:
            return -1
        elif number == list_1[mid]:
            return mid
        elif number > list_1[mid]:
            i += mid
            return i + Binary_search(number,list_1[mid:])
        else:
            return i + Binary_search(number,list_1[:mid])

if __name__ == '__main__':
    assert (Binary_search(5, (1, 3, 7)) == 1)
    assert (Binary_search(1, (1, 3, 7)) == 0)
    assert (Binary_search(7, (1, 3, 7)) == 2)
    assert (Binary_search(8, (1, 3, 7)) == 2)
    assert (Binary_search(0, (1, 3, 7)) == -1)
    Binary_search("abc", (1, 3, 7))