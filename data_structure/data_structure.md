# Data structure with Python

- 엄밀히 말하면 이 둘은 다르지만 밀접한 관련이 있음
  - 자료구조 : 데이터를 어떤 구조로 저장하고 탐색해야 효율적인가?
  - 알고리즘 : 문제를 해결하는 방법론

- 자료구조의 알고리즘 - 데이터를 저장하고 탐색하는 방법에 대한 고민들
- 자료구조를 이용한 알고리즘 - 자료구조를 이용해 어떤 문제를 해결하는 것

## Linked List 탄생 배경

- 배열은 할당할 때 크기를 지정해줘야한다는 치명적인 단점이 있음
  데이터를 스택영역에 미리 크기를 만들어서 할당을 하는 방법이기 때문

- 즉, 배열은 한 번 할당을 하면 줄이고 늘릴 수 없기 때문에 LinkedList가 생겼다

- 필요한 데이터가 매 번 다른 경우, 데이터가 늘어나면 바로 이어주기만 하면 되고, 필요 없으면 바로 지워서 다시 참조를 통해 연결시켜주기만 하면 된다.

- 가변배열처럼 탐색, 할당, 복사, 삭제 등의 리소스 낭비가 전혀 없다

		ex)	int num = 5;
	​	int arr[num]; ==> 이렇게 num이라는 변수를 넣게되면
	​				변수는 가변적이라서 에러가 남
	​				배열은 고정된 수, 정해진 수, 상수로 지정해줘야 됨

- 가변배열은 원래배열에 추가를 시킬 수 있는 것이 아니라 줄이거나 늘릴 메모리 공간을 찾아서(탐색) (할당)하고 원래 데이터를 (복사)하고 (삭제)를 하는 일련의 과정을 거치기 때문에 리소스 낭비가 엄청나다. 어쩔 수 없이 쓸 경우가 있지만 웬만하면 안 쓰는 것이 좋다

- 하지만 배열이 무조건 안 좋고 LinkedList가 무조건 좋은게 아니라, 상황에 따라 적절한 자료구조를 사용하는게 좋다.
  예를 들어, 배열을 사용하면 유관데이터를 메모리에 순차적으로 쭉 나열할 수 있어서 CacheHit가능성이 커져서 성능향상에 도움이 된다

- 자료구조의 구성

  - Insert	데이터를 어떻게 저장할 것인가?

  	 Search	데이터를 어떻게 탐색할 것인가?

  	 Delete	데이터를 어떻게 삭제할 것인가?

  - ADT AbstractDataType추상자료형 // 함수를 어떻게 만들건지 UI목록이라고 보면 됨

    DummyLinkedList
    ​	생성자
    ​	add		void add(data)
    ​	first		return data bool
    ​	next		return data bool
    ​	delete		return data

- linked_list 구현

  ```python
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
          
          dummy = Node("Dummy")	// Dummy라는 데이터를 가진 첫 번째 노드 생성, 아무 의미없는 노드
          self.head = dummy
          self.tail = dummy

      #insert, 노드 추가하는 함수
      def add(self, data):
          newNode = Node(data)		// Node클래스의 인스턴스 newNode 생성, 새 노드 생성 후
          self.tail.next = newNode		// 새 노드를 리스트에 이어줌
          self.tail = newNode			// 새로 추가된 노드이기 때문에 맨 마지막 tail이 됨
          self.numOfData += 1		// 노드 갯수, 즉 데이터 갯수 추가

      #search part1, 노드 처음부터 탐색 함수
      def first(self):
          self.before = self.head		// before는 항상 current노드 이전에 오게 설정
          self.current = self.head.next	// 첫 번째 탐색이기때문에 current는 head.next
          if self.current == None:       	// if not self.current 이렇게 해도 됨
              return self.current, False	// 없는 데이터 값이랑 bool 반환
          return self.current.data, True	// current데이터와 bool 반환
          
      #search part2, 탐색을 한 노드 다음부터 탐색 함수
      def next(self):
          if self.current.next == None: 		// if not self.current.next 이렇게 해도 됨
              return self.current.next, False
          self.before = self.current			// current 다음 노드로 한 칸씩 이동하니까 before가 current
          self.current = self.current.next	// current 다음 노드로 current 이동
          return self.current.data, True		// 다음으로 이동한 current데이터와 bool 반환

      #delete, 노드 삭제 함수
      def delete(self):
          '''
          #refcount가 0이 되면서 garbage collector에 의해 사라진다		// 이렇게 해도 되지만 아직 안 배워서
          retData = self.current.data							// return할 데이터 따로 저장
          self.before.next = self.current.next						// before와 삭제할노드 다음 노드를 이어줌
          self.current = self.before								// 삭제 후 current를 꼭 before노드로 이동
          self.numOfData -= 1								// 그래야지 그 다음 노드를 반환할 수 있음
          return retData										// 조심할 것
          '''

          delNode = self.current				// 삭제할 노드를 delNode로 참조를 해줌
          retData = self.current.data			// return할 데이터 따로 저장
          self.before.next = self.current.next		// before와 삭제할노드 다음 노드를 이어줌
          self.current = self.before				// 삭제 후 다음 노드를 반환하기 위해 꼭 before로 current이동할 것
          del delNode						// 노드 삭제
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
  ```


## Stack, Queue

- 리스트 사용하여 Stack 기능 구현

  ```python
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
  ```

- 리스트 사용하여 Queue 기능 구현

  ```python
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
  ```

## 후위표기법

- 후위표기법 계산기
  중위표기법으로 수식입력받고, 후위표기법으로 변환한 뒤, 계산하는 클래스
  수식을 입력받을 때, 한자리수만 입력받는다고 가정하에 만듬

  ```python
  class Calculator:
      def __init__(self, exp):
          self.orgExp = exp.replace(" ", "") 		// 띄어쓰기해도 상관없게 만듬
          #self.postfixExp = exp

      def GetWeight(self, oprt):
          if oprt == '*' or oprt == '/':
              return 9
          elif oprt =='+' or oprt =='-':
              return 7
          elif oprt == '(':
              return 5
          else:
              return -1

      def ConvertToPostfix(self):
          listExp = []
          listStack = []

          for ch in self.orgExp:
              if ch.isdigit():
                  listExp.append(ch)
              else:
                  if self.GetWeight(ch) == 5 or not listStack:
                      listStack.append(ch)
                  elif ch == ')':
                      while 1:
                          op = listStack.pop()
                          if op == '(':
                              break
                          listExp.append(op)
                          
                  elif self.GetWeight(ch) > self.GetWeight(listStack[-1]):
                      listStack.append(ch)
                  elif self.GetWeight(ch) == self.GetWeight(listStack[-1]):
                      listExp.append(listStack.pop())
                      listStack.append(ch)
                  elif self.GetWeight(ch) < self.GetWeight(listStack[-1]):
                      listExp.append(listStack.pop())
                      listStack.append(ch)

          if listStack:
              while listStack:
                  listExp.append(listStack.pop())

          self.postfixExp = "".join(listExp)
          return self.postfixExp

      def calcTwoOp(self, op1, op2, oprt):
          if oprt == "+":
              return op1 + op2
          elif oprt == "-":
              return op1 - op2
          elif oprt == "*":
              return op1 * op2
          elif oprt == "/":
              return op1 // op2
      
      def Calculate(self):
          #list for stack
          stackOperand = [] //후위표기법 수식에서 2개의 숫자를 임의로 스택에 저장할 용도,연산자만나면 2개 pop해서 계산
          for ch in self.postfixExp:
              #If it is a number under 10, prepare calculation
              if ch.isdigit():
                  stackOperand.append(int(ch))
              #If it is an operand which is not number, do calculate
              else:
                  op2 = stackOperand.pop()
                  op1 = stackOperand.pop()
                  result = self.calcTwoOp(op1, op2, ch)
                  stackOperand.append(result)
          return result

  if __name__ == "__main__":
      calc = Calculator(input("Input : "))
      print(calc.ConvertToPostfix())
      result = calc.Calculate()
      print(result)
  ```

## Heap, PriorityQueue

- Heap

  ```python
  class Heap:
      def GetParentIdx(self, idx):			// 부모노드의 인덱스 반환
          return idx // 2
      def GetLeftChildIdx(self, idx):			// 왼쪽자식노드의 인덱스 반환
          return idx * 2
      def GetRightChildIdx(self, idx):		// 오른쪽자식노드의 인덱스 반환
          return idx * 2 + 1
      
      def __init__(self, s_min_max = "min"):
          self.dynamicArr = [None]		// DynamicArray의 역할을 리스트가 하게 설정
  										// 맨 마지막 노드의 index와 일치시키기 위해 Null값 할당
          self.numOfData = 0				// heap에서의 노드 갯수
          
          if s_min_max == "min":			// 최소 힙 아니면 최대 힙을 나타내는 flag 역할
              self.min_max = 1			// 1 : min heap(최소 힙), 2 : max heap(최대 힙)
          elif s_min_max == "max":
              self.min_max = 2
          else:
              self.min_max = 1
  
      def IsEmpty(self):				// 노드가 아무 것도 없는지 확인, 데이터가 아무 것도 없는지 확인
          if self.numOfData == 0:
              return True
          return False
  
      def GetNumOfData(self):				// 노드의 갯수 반환, 데이터의 갯수 반환
          return self.numOfData			// 즉, 마지막 노드의 인덱스 반환
  
      def IsGoUp(self, idx, data): 		// 새로운 노드를 추가했을 때, 부모노드와 비교해서 위로 올릴지 냅둘지 판단하는 함수
          if idx == 1:					// 노드의 인덱스가 1인 것은, 노드가 하나만 있고 더이상 올라갈 수 없음을 의미
              return False
  
          value = self.dynamicArr[self.GetParentIdx(idx)] // 현재노드의 데이터와 비교하기 위해 부모노드의 값을 불러옴
          
          if self.min_max == 1:		// 최소힙이면 부모노드보다 현재노드 값이 작으면 위로 올리면 됨
              if value > data:
                  return True
              return False
          elif self.min_max == 2:		// 최대힙이면 부모노드보다 현재노드 값이 크면 위로 올리면 됨
              if value < data:
                  return True
              return False
      
      def Insert(self, data):
          if self.IsEmpty():				// 힙 트리에 아무 노드도 없을 경우 그냥 바로 insert하면 됨
              self.dynamicArr.append(data)
              self.numOfData += 1			// 노드가 추가됐으니 데이터 갯수 올림
              return
              
          self.dynamicArr.append(data)		// 힙에서 insert할 때, 새로운 노드는 맨 마지막에 추가시킨 후
          self.numOfData += 1			// 부모노드와 하나씩 비교하면서 올릴지 냅둘지 결정
          								// 노드가 추가됐으니 데이터 갯수 올림
          t_idx = self.numOfData			// 새로 추가된 현재 노드의 인덱스 따로 저장
          
  	// 새로 추가된 현재 노드가 올라갈 수 있는지 없는지 함수로 판단해서
  	// 부모노드에서 내려온 값들은 바로바로 저장을 하면 되지만, 성능향상을 고려해서
  	// 새로 추가된 노드의 값은 더이상 올라갈 수 없는 부모노드의 위치에 마지막에 한 번만 할당
  	// 현재노드의 값과 부모노드의 값을 매번 바꿔줄 필요가 없기때문에
          while self.IsGoUp(t_idx, data):
              self.dynamicArr[t_idx] = self.dynamicArr[self.GetParentIdx(t_idx)]
              t_idx = self.GetParentIdx(t_idx)
  
      // 마지막에 더이상 올라갈 수 없는 부모노드에 새로 추가된 현재 노드의 값을 넣어주면 된다
  	// numOfData 값 줄여주기 전에 새로 추가된 데이터 값을 미리 받아놓고 그 값을 넣어주는 것 주의
  	self.dynamicArr[t_idx] = data
  
      def WhichIsPriorChild(self, idx):		// delete하고 부모노드와 자식노드 위치바꾸면서, left와 right 중에서 뭘 비교를 할 지 골라주는 함수
          left_idx = self.GetLeftChildIdx(idx)		// left자식노드 값 반환
          right_idx = self.GetRightChildIdx(idx)	// right자식노드 값 반환
          if left_idx > self.numOfData:			// 단말노드인 경우
              return -1
          elif left_idx == self.numOfData:	// 자식노드가 하나만 있고, 마지막 노드인 경우
              return left_idx
          elif left_idx < self.numOfData:		// 자식노드가 두 개가 있는 경우이고, 비교를 해서 뭐랑 비교를 할지 골라야함
              if self.min_max == 1:			// 최소힙이냐 최대힙이냐에 따라 비교를 하는 대상이 달라짐
                  if self.dynamicArr[left_idx] <= self.dynamicArr[right_idx]:
                      return left_idx
                  elif self.dynamicArr[left_idx] > self.dynamicArr[right_idx]:
                      return right_idx
              elif self.min_max == 2:
                  if self.dynamicArr[left_idx] <= self.dynamicArr[right_idx]:
                      return right_idx
                  elif self.dynamicArr[left_idx] > self.dynamicArr[right_idx]:
                      return left_idx
  
      def IsGoDown(self, idx, data):		// delete후에 제일 처음으로 올려진 마지막 노드를 내릴지 결정하는 함수
          child_idx = self.WhichIsPriorChild(idx)	// 비교를 할 자식노드의 인덱스를 따로 저장해둠
          
          if child_idx < 0:				// 자식노드가 없다면 바꿔줄 필요가 없음
              return False
          
  		#// 자식노드가 있을 경우
  		#// 현재노드와 비교를 하기위해 골라낸 자식노드의 값
          value = self.dynamicArr[self.WhichIsPriorChild(idx)]
          
          if self.min_max == 1:
              if value < data:
                  return True
              elif value == data:
                  return False
              return False
          elif self.min_max == 2:
              if value > data:
                  return True
              elif value == data:
                  return False
              return False
              
      def Delete(self):
          if self.IsEmpty():				#// 노드가 아무 것도 없으면 지울게 없음
              print("Nothing to delete")
              return
          elif self.numOfData == 1:		#// 노드가 하나면 지우고 값만 반환하고, 노드위치를 바꾸줄 필요가 없음
              self.numOfData -= 1
              return self.dynamicArr[1]
  	
  	#// 출력하는 제일 위의 노드 값을 미리 저장을 해둠,,,힙트리에서 값을 출력하고 삭제함
  	#// 삭제 후에 맨 뒤 쪽의 노드 값을 맨 위로 올려서, 자식노드와 하나씩 비교해서 내릴지 결정
  	retData = self.dynamicArr[1]
          data = self.dynamicArr[self.numOfData]
          self.numOfData -= 1
  
          t_idx = 1
          while self.IsGoDown(t_idx, data):
              self.dynamicArr[t_idx] = self.dynamicArr[self.WhichIsPriorChild(t_idx)]
              t_idx = self.WhichIsPriorChild(t_idx)
          self.dynamicArr[t_idx] = data		#// 마지막에 더이상 내려갈 수 없는 자식노드에 오면 현재노드의 값 넣어줌 #// 성능향상을 고려해서
          return retData
  
  
  if __name__ == "__main__":
      heap = Heap("min")
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
  ```

- PriorityQueue

  - Heap과 PriorityQueue는 이름만 다르고 완벽하게 동일한 것임
  - PriorityQueue는 우선순위에 따라 값을 빼서 쓰는 것이기 때문에

  ```python
  from heap import Heap
  
  class PriorityQueue:
      def __init__(self, s_min_max = "min"):
          self.heap = Heap(s_min_max)		// 객체합성을 했다고 보면 됨
  
      def IsEmpty(self):
          return self.heap.IsEmpty()
  
      def GetNumOfData(self):
          return self.heap.GetNumOfData()
  
      def Enqueue(self, data):
          self.heap.Insert(data)
  
      def Dequeue(self):
          return self.heap.Delete()
  ```

- 