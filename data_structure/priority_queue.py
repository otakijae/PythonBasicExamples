from heap import Heap

class PriorityQueue:
    def __init__(self, s_min_max = "min"):
        self.heap = Heap(s_min_max)

    def IsEmpty(self):
        return self.heap.IsEmpty()

    def GetNumOfData(self):
        return self.heap.GetNumOfData()

    def Enqueue(self, data):
        self.heap.Insert(data)

    def Dequeue(self):
        return self.heap.Delete()

if __name__ == "__main__":
    pq = PriorityQueue("min")
    pq.Enqueue(3)
    pq.Enqueue(7)
    pq.Enqueue(2)
    pq.Enqueue(1)
    pq.Enqueue(9)
    pq.Enqueue(5)
    pq.Enqueue(8)
    pq.Enqueue(10)
    pq.Enqueue(5)
    pq.Enqueue(6)
    pq.Enqueue(4)

    ndata = pq.GetNumOfData()

    for i in range(1, ndata+1):
        print(pq.heap.dynamicArr[i])

    print("\n\n")

    for i in range(1, ndata+1):
        print(pq.Dequeue())
