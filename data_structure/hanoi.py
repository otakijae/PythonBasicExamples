def hanoi(num, _from, _by, _to):    #number of plates
    if num == 1:
        print("{}th plate moved from {} to {}".format(num, _from, _to))
        return
    hanoi(num-1, _from, _to, _by)
    print("{}th plate moved from {} to {}".format(num, _from, _to))
    hanoi(num-1, _by, _from, _to)

if __name__ == "__main__":
    while 1:
        numOfTray = int(input("Input the number of plates!(Exit : 0) :"))
        if numOfTray == 0:
            break
        hanoi(numOfTray, 'A', 'B', 'C')
