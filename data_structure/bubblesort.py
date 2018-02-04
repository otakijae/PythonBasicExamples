def BubbleSort(li):
    list_length = len(li)
    
    for i in range(list_length-1):
        for j in range(list_length-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

if __name__ == "__main__":
    li = [2, 3, 1, 4]
    BubbleSort(li)
    print(li)
