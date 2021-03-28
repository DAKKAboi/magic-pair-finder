def mergeSort(list):

    import math

    def merge (list, start, mid, end):

        lenL = mid - start + 1
        lenR = end - mid

        leftList = list[start:mid+1]
        rightList = list[mid+1:end+1]

        i = 0
        j = 0

        k = start
        while k <= end:

            if leftList[i] <= rightList[j]:
                list[k] = leftList[i]
                i = i + 1

            else:
                list[k] = rightList[j]
                j = j + 1

            if i == lenL:
                l = j
                while l < lenR:
                    list[start + lenL + l] = rightList[l]
                    l = l + 1
                k = end + 2

            if j == lenR:
                l = i
                while l < lenL:
                    list[l + lenR + start] = leftList[l]
                    l = l + 1
                k = end + 2
            k = k + 1

        return list

    def sort(list, start, end):    
        if start < end:
            mid = math.floor((start+end)/2)
        
            sort(list, start, mid)
            sort(list, mid + 1, end)
        
            merge(list, start, mid, end)

        return list
    sort(list, 0, len(list)-1)
    return list
