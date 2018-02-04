class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.numOfData = 0
        self.current = None
        self.before = None
        self.head = None
        self.tail = None
        
        dummy = Node("Dummy")
        self.head = dummy
        self.tail = dummy

    #insert
    def add(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode
        self.numOfData += 1

    #search part1
    def first(self):
        self.before = self.head
        self.current = self.head.next
        if self.current == None:       #if not self.current
            return self.current, False
        return self.current.data, True
        
    #search part2
    def next(self):
        if self.current.next == None:  #if not self.current.next
            return self.current.next, False
        self.before = self.current
        self.current = self.current.next
        return self.current.data, True

    #delete
    def delete(self):
        '''
        #refcount가 0이 되면서 garbage collector에 의해 사라진다
        retData = self.current.data
        self.before.next = self.current.next
        self.current = self.before
        self.numOfData -= 1
        return retData
        '''
        delNode = self.current
        retData = self.current.data

        self.before.next = self.current.next
        self.current = self.before

        del delNode
        self.numOfData -= 1

        return retData
        


if __name__ == "__main__":
    lis = LinkedList()
    lis.add(2)
    lis.add(3)
    lis.add(1)
    lis.add(5)
    lis.add(10)
    lis.add(7)
    lis.add(2)

    print("데이터의 개수 : {}".format(lis.numOfData))
    
    data, b_ret = lis.first()       # bool, data value // explore from the first
    if b_ret:                       # if True
        print(data, "      ")
        data, b_ret = lis.next()
        while b_ret:                # while True // explore from already explored one
            print(data, "     ")
            data, b_ret = lis.next()

    print("\n")
    
    data, b_ret = lis.first()
    if b_ret:       # if True
        if data == 2:
            lis.delete()
            
        data, b_ret = lis.next()
        while b_ret:    # while True
            if data == 2:
                lis.delete()
            data, b_ret = lis.next()

    print("데이터의 개수 : {}".format(lis.numOfData))
    data, b_ret = lis.first()
    if b_ret:
        print(data, "      ")
        data, b_ret = lis.next()
        while b_ret:
            print(data, "     ")
            data, b_ret = lis.next()

        print("\n")
