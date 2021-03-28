def findSplit(list, token):#the list is ordered
    length = len(list)
    i = 0

    while i <= length - 1:
        if list[i] > token:
            break
        i = i + 1
    return i


