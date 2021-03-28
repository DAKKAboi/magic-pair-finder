def binarySearch(list, item):#list is an ordered list, item is what is being searched for
    length = len(list)
    import math

    def iterator(min, max):
        mid = math.floor((min+max)/2)

        if list[mid] == item:
            return mid
        elif list[mid] < item:
            mid = iterator(mid + 1, max)
        else:
            mid = iterator(min, mid - 1)
        if min == max and min != item:
            mid = -1
        return mid

    if float(item) > float(list[-1]) or float(item) < float(list[0]):
        return None
    else:
        location = iterator(0, length - 1)

    if list[location] == item:
        return location
    else:
        return None


