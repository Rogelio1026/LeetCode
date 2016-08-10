def Binary_search(number,list_1):
    """

    :param number: int
    :return: tuple
    """
    i = 0
    mid = len(list_1)/2
    if number > list_1[-1]:
        return len(list_1)-1
    if number < list_1[0]:
        return -1
    if number == list_1[mid]:
        return mid
    elif number > list_1[mid]:
        i += mid
        Binary_search(number,list_1[mid:])
    else:
        Binary_search(number,list_1[:mid])