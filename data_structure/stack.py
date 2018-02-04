class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    #Initialize
    def __init__(self):
        self.head = None

    #Check if stack is empty
    def IsEmpty(self):
        if not self.head:
            return True
        return False

    #insert
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    #delete & search
    def pop(self):
        if self.IsEmpty():  #if not self.head:
            print("There is no data!")
            exit(1)
        delNode = self.head
        retData = self.head.data
        self.head = self.head.next
        del delNode
        return retData

    #search what data is on the top
    def peek(self):
        if self.IsEmpty():  #if not self.head:
            print("There is no data!")
            exit(1)
        retData = self.head.data
        return retData

if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    while not stack.IsEmpty():
        print(stack.pop())

    stack.peek()
