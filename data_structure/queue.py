class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    #Initialize
    def __init__(self):
        self.head = None
        self.tail = None

    def IsEmpty(self):
        if not self.head:
            return True
        return False

    #insert
    def Enqueue(self, data):
        newNode = Node(data)
        
        if self.IsEmpty():
            self.head = newNode
            self.tail = newNode
            return
            
        self.tail.next = newNode
        self.tail = newNode

    #delete & search
    def Dequeue(self):
        if self.IsEmpty():
            print("There is no data!")
            exit(1)
        delNode = self.head
        retData = self.head.data
        self.head = self.head.next
        del delNode
        return retData

    def peek(self):
        if self.IsEmpty():
            print("There is no data!")
            exit(1)
        retData = self.head.data
        return retData


if __name__ == "__main__":
    queue = Queue()

    queue.Enqueue(1)
    queue.Enqueue(2)
    queue.Enqueue(3)
    queue.Enqueue(4)
    queue.Enqueue(5)

    while not queue.IsEmpty():
        print(queue.Dequeue())

    queue.peek()
