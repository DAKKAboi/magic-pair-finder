from BinarySearch import binarySearch
from RandomListGenerator import listGen
import ListSplit

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


randList = listGen(10,0,9)
print(randList)
sortedList = mergeSort(randList)

searchToken = str(input('please enter the number to find pairs for  '))
halfway = float(searchToken)/2
splitPoint = ListSplit.findSplit(sortedList,halfway)

greaterList = sortedList[splitPoint + 1 : len(sortedList)]

i = 0
while i <= splitPoint:
    pair = int(searchToken) - sortedList[i]
    location = binarySearch(greaterList, pair)
    if location == None:
        i = i + 1
    else:
        location = location + splitPoint
        break

if location != None:
    print(str(sortedList[i]) + ' + ' + str(sortedList[location]) + ' = ' + str(searchToken))
else:
    print('no pairs found')