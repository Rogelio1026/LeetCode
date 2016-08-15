def Binary_search(number,list_1):
    mid = len(list_1)/2
    i = 0
    while number > list_1[i]:
        if number > list_1[-1] or number < list_1[i+1]:
            return i
        elif number == list_1[mid]:
            i = mid
            return i
        elif number > list_1[mid]:
            list_1 = list_1[mid:]
            i += mid
        elif number < list_1[mid]:
            list_1 = list_1[:mid]

if __name__ == '__main__':
    print(Binary_search(5,[1,3,5]))