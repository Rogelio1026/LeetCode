def Binary_search(number,list_1):
    first = 0
    last = len(list_1)-1
    while first <= last:
        mid = (first+last)/2
        if number == list_1[mid]:
            return mid
        elif number > list_1[mid]:
            first = mid + 1
        elif number < list_1[mid]:
            last = mid -1
    if number < list_1[0]:
        return -1
    else:
        return first-1

if __name__ == '__main__':
    print(Binary_search(5,[1,3,5,7,9]))