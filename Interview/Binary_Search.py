def Binary_search(number,list_1):
    """

    :param number: int
    :return: int
    """
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
    print(Binary_search(9,(1,3,5,7,9)))
    assert(Binary_search(5,(1,3,7))==1)