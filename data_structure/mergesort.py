def MergeTwoSection(unsorted_list, start, mid, end):
    leftIdx = start
    rightIdx = mid + 1
    numOfData = (end - start) + 1

    temp_list=[0 for i in range(numOfData+1)]

    tempIdx = 0

    for i in range(numOfData):
        if unsorted_list[leftIdx] < unsorted_list[rightIdx]:
            temp_list[i] = unsorted_list[leftIdx]
            leftIdx+=1

            if leftIdx > mid:
                tempIdx = i+1
                break
        else:
            temp_list[i] = unsorted_list[rightIdx]
            rightIdx+=1

            if rightIdx > end:
                tempIdx = i + 1
                break
            
    if leftIdx > mid:
        for i in range(rightIdx, end+1):
            temp_list[tempIdx] =unsorted_list[i]
            tempIdx+=1
    elif rightIdx > end:
        for i in range(leftIdx, mid+1):
            temp_list[tempIdx] = unsorted_list[i]
            tempIdx+=1

    tempIdx = 0
    
    for i in range(start, end+1):
        unsorted_list[i] = temp_list[tempIdx]
        tempIdx+=1

    del temp_list

def mergesort(unsorted_list, start, end):
    if start >= end:
        return

    mid = (start + end) // 2

    mergesort(unsorted_list, start, mid)
    mergesort(unsorted_list, mid+1, end)

    MergeTwoSection(unsorted_list, start, mid, end)

if __name__ == "__main__":
    unsorted = [8, 3, 7, 1, 2, 6, 4, 5]
    end = len(unsorted)-1
    mergesort(unsorted, 0, end)
    print(unsorted)
