class Heap:
    def GetParentIdx(self, idx):
        return idx // 2
    def GetLeftChildIdx(self, idx):
        return idx * 2
    def GetRightChildIdx(self, idx):
        return idx * 2 + 1
    
    def __init__(self, s_min_max = "min"):
        self.dynamicArr = [None]
        self.numOfData = 0
        if s_min_max == "min":
            self.min_max = 1
        elif s_min_max == "max":
            self.min_max = 2
        else:
            self.min_max = 1

    def IsEmpty(self):
        if self.numOfData == 0:
            return True
        return False

    def GetNumOfData(self):
        return self.numOfData

    def IsGoUp(self, idx, data):
        if idx == 1:
            return False

        value = self.dynamicArr[self.GetParentIdx(idx)]
        
        if self.min_max == 1:
            if value > data:
                return True
            return False
        elif self.min_max == 2:
            if value < data:
                return True
            return False
    
    def Insert(self, data):
        if self.IsEmpty():
            self.dynamicArr.append(data)
            self.numOfData += 1
            return
            
        self.dynamicArr.append(data)
        self.numOfData += 1
        
        t_idx = self.numOfData
        
        while self.IsGoUp(t_idx, data):
            self.dynamicArr[t_idx] = self.dynamicArr[self.GetParentIdx(t_idx)]
            t_idx = self.GetParentIdx(t_idx)
        self.dynamicArr[t_idx] = data

    def WhichIsPriorChild(self, idx):
        left_idx = self.GetLeftChildIdx(idx)
        right_idx = self.GetRightChildIdx(idx)
        if left_idx > self.numOfData:
            return -1
        elif left_idx == self.numOfData:
            return left_idx
        elif left_idx < self.numOfData:
            if self.min_max == 1:
                if self.dynamicArr[left_idx] <= self.dynamicArr[right_idx]:
                    return left_idx
                return right_idx
            elif self.min_max == 2:
                if self.dynamicArr[left_idx] <= self.dynamicArr[right_idx]:
                    return right_idx
                return left_idx

    def IsGoDown(self, idx, data):
        child_idx = self.WhichIsPriorChild(idx)
        
        if child_idx < 0:
            return False
        
        value = self.dynamicArr[self.WhichIsPriorChild(idx)]
        
        if self.min_max == 1:
            if value < data:
                return True
            return False
        elif self.min_max == 2:
            if value > data:
                return True
            return False
            
    def Delete(self):
        if self.IsEmpty():
            print("Nothing to delete")
            return
        elif self.numOfData == 1:
            self.numOfData -= 1
            return self.dynamicArr[1]

        retData = self.dynamicArr[1]
        data = self.dynamicArr[self.numOfData]
        self.numOfData -= 1

        t_idx = 1
        while self.IsGoDown(t_idx, data):
            self.dynamicArr[t_idx] = self.dynamicArr[self.WhichIsPriorChild(t_idx)]
            t_idx = self.WhichIsPriorChild(t_idx)
        self.dynamicArr[t_idx] = data

        return retData


if __name__ == "__main__":
    heap = Heap("max")
    heap.Insert(3)
    heap.Insert(5)
    heap.Insert(1)
    heap.Insert(10)
    heap.Insert(8)
    heap.Insert(7)
    heap.Insert(4)
    heap.Insert(5)
    heap.Insert(2)
    heap.Insert(6)
    heap.Insert(9)

    ndata = heap.GetNumOfData()

    #insert가 잘 되었는지 테스트 코드
    for i in range(1, ndata+1):
        print(heap.dynamicArr[i])

    print("\n\n")

    #delete가 잘 되었는지 테스트
    for i in range(1, ndata+1):
        print(heap.Delete())
        
