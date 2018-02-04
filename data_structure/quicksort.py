def get_pivot(li, start, end):
    '''
    mid = (start + end)//2
    list_idx = [start, mid, end]
    
    if li[list_idx[0]] > li[list_idx[1]]:
        list_idx[0], list_idx[1] = list_idx[1], list_idx[0]
    if li[list_idx[1]] > li[list_idx[2]]:
        list_idx[1], list_idx[2] = list_idx[2], list_idx[1]
    if li[list_idx[0]] > li[list_idx[1]]:
        list_idx[0], list_idx[1] = list_idx[1], list_idx[0]

    return list_idx[1]
    '''
    mid = (start + end) // 2
    li = [start, mid, end]
    li.sort()
    return li[1]
    
def exchange(li, start, end):
    #global call_of_exchange
    #call_of_exchange += 1
    
    idx_pivot = get_pivot(li, start, end)
    li[start], li[idx_pivot] = li[idx_pivot], li[start]

    pivot = li[start]
    low = start + 1
    high = end

    while low <= high:
        while low <= end and li[low] <= pivot:
            low+=1
        while high >= (start + 1) and li[high] >= pivot:
            high-=1
        if low <= high:
            li[low], li[high] = li[high], li[low]

    li[start], li[high] = li[high], li[start]

    return high

def quicksort(li, start, end):
    if start >=end:
        return

    idx_pivot = exchange(li, start, end)

    quicksort(li, start, idx_pivot - 1)
    quicksort(li, idx_pivot + 1, end)

if __name__ == "__main__":
    li = [5,2,8,7,3,6,3,7,1,8]
    end = len(li)-1
    quicksort(li, 0, end)
    print(li)
    #print(call_of_exchange)
