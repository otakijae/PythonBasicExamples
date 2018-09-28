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

​	ex)	int num = 5;
		int arr[num]; ==> 이렇게 num이라는 변수를 넣게되면
					변수는 가변적이라서 에러가 남
					배열은 고정된 수, 정해진 수, 상수로 지정해줘야 됨

- 가변배열은 원래배열에 추가를 시킬 수 있는 것이 아니라 줄이거나 늘릴 메모리 공간을 찾아서(탐색) (할당)하고 원래 데이터를 (복사)하고 (삭제)를 하는 일련의 과정을 거치기 때문에 리소스 낭비가 엄청나다. 어쩔 수 없이 쓸 경우가 있지만 웬만하면 안 쓰는 것이 좋다

- 하지만 배열이 무조건 안 좋고 LinkedList가 무조건 좋은게 아니라, 상황에 따라 적절한 자료구조를 사용하는게 좋다.
  예를 들어, 배열을 사용하면 유관데이터를 메모리에 순차적으로 쭉 나열할 수 있어서 CacheHit가능성이 커져서 성능향상에 도움이 된다

- 자료구조의 구성

  - Insert	데이터를 어떻게 저장할 것인가?

  - Search	데이터를 어떻게 탐색할 것인가?

  - Delete	데이터를 어떻게 삭제할 것인가?

  - ADT AbstractDataType추상자료형 // 함수를 어떻게 만들건지 UI목록이라고 보면 됨

    DummyLinkedList
    	생성자
    	add		void add(data)
    	first		return data bool
    	next		return data bool
    	delete		return data

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

  ​