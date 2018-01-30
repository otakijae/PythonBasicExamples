# PythonBasicExamples
파이썬 기본 문법 정리 / Python basic examples
- 파이썬 기본 문법 및 유의할 점 정리

## Python은?
1989년 크리스마스 연휴를 보내던 Guido van Rossum이 만든 고급 프로그래밍 언어

- 특징
	- 인터프리터
	- 객체지향
	- 동적타이핑
	- 엄격한 문법

- REPL - Read - Eval - Print Loop
코드를 입력하면 바로 결과를 확인할 수 있음


- Python version 확인 및 잡다한 기능
```
$ python3
Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()

$ python3.6
Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

- Print something / Interpreter Language
```
>>> print("hello world!")
hello world!

>>> a=10
>>> print(a)
10

>>> a = "I am your father!"
>>> print(a)
I am your father!
>>> print(a[3])
m
>>> a[3] = 'a'				// Python에서 string 변수 변경 불가함 🇺🇸🇺🇸🇺🇸
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

>>> print(10+4)
14
>>> print(10-4)
6
>>> print(10*4)
40
>>> print(10/4)	실수형나누기 / 정수나누기정수가 실수로 나오니까 / ‘/’라는 명령에 따라 타입을 바꿈 / 동적타이핑
2.5
>>> print(10//4)	정수형나누기 / 정수나누기정수가 정수로 나오도록
2

>>> 10>4
True
>>> a = 10>4
>>> print(a)
True
>>> a=10
>>> b=10
>>> a==b
True
>>> a=b
>>> a==b
True
>>> a!=b
False
>>> a=10 b=10 a==b	// 한 줄에 다 못씀
  File "<stdin>", line 1
    a=10 b=10 a==b
         ^
SyntaxError: invalid syntax

>>> a=10 
>>> b=10
>>> a==b
True
```

- 객체 생성 및 할당 쉽게(객체 할당하는 것을 스티커를 붙여준다고 생각하면 쉽게 이해됨)
```
>>> a=10		// 상수 객체의 공간을 만들어서 a라는 스티커를 붙여 이름을 정함
>>> b=10		// a의 값과 같은 값을 가지고 있어서, 같은 객체의 공간에 b라는 스티커를 붙여 다른 이름을 정해줌
>>> print(id(a), ' ', id(b))		
4297624224   4297624224
>>> a = 15
>>> print(id(a), ' ', id(b))
4297624384   4297624224	// a의 값이 변경돼서, 다른 주소가 출력이 됨
```

- String
```
>>> hello = "Hello"
>>> world = 'World'
>>> print(hello + world)
HelloWorld
>>> print(hello , world)
Hello World
>>> a = "hello"
>>> b = "world"
>>> c=a+b
>>> print(c)
helloworld

>>> c = a,b
>>> print(c)
('hello', 'world')
>>> print(a,b)
hello world

>>> print('*' * 50)	//문자열 곱하기
**************************************************

>>> a = "pen"
>>> b = "apple"
>>> print("I have a %s and I have an %s \n" % (a,b) )	// C언어 ‘,’ 대신에 ‘%’로
I have a pen and I have an apple 

>>> print("I have a %s and I have an %s \n"% a,b )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not enough arguments for format string
```

- Python의 신기하고 유용한 메소드들
```
>>> s = "python is, easy to learn, however powerful"
>>> s.count('p')
2
>>> s.find('i')
7
>>> s.find('p')
0
>>> s2 = ','.join('python') 
>>> s2
'p,y,t,h,o,n'
>>> s2 = ' '.join(s)
>>> s2
'p y t h o n   i s ,   e a s y   t o   l e a r n ,   h o w e v e r   p o w e r f u l'
>>> s2 = ','.join(s)
>>> s2
'p,y,t,h,o,n, ,i,s,,, ,e,a,s,y, ,t,o, ,l,e,a,r,n,,, ,h,o,w,e,v,e,r, ,p,o,w,e,r,f,u,l'

>>> li = s.split(s)	// string s 기준으로 split을 해서 아무것도 안 나눠짐
>>> li
['', '']
>>> li = s.split(',')	// ‘ , ’를 기준으로 split함
>>> li
['python is', ' easy to learn', ' however powerful']
>>> for l in li :
...     print(l)
... 
python is
 easy to learn
 however powerful

>>> s = "I am a, boy"
>>> s.split()				// 원본은 변경이 안 됨🇪🇹🇪🇹🇪🇹String은 변경불가
['I', 'am', 'a,', 'boy']
>>> s
'I am a, boy'

>>> result_s = s.split()		// split한 것을 객체에 저장을 하려면 이렇게
>>> result_s
['I', 'am', 'a,', 'boy']


>>> s
'python is, easy to learn, however powerful'
>>> s.replace('python', 'C++')
'C++ is, easy to learn, however powerful'

s.count('p')
s.find('i')
s2 = ','.join('python') // s2 = ' '.join(s)
li = s.split(',') // li = s.split()
S.replace(‘python’ , ’C++’)
```

---

- Python 2.7.10은 맥에서 기본 내장된 Python이기 때문에 다운받은 Python2.7이나 Python3.6을 간단하게 python명령으로 실행시키려면 아래와 같이 하면 된다. 나중에 Python 가상 개발 환경을 세팅을 해야되는데 일단은 간단하게 이렇게 실행하면 쉽다.
```
$ python --version
Python 2.7.10
$ alias python=python3.6
$ python --version
Python 3.6.0
$ python
Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

- List []
```
>>> animal = ['lion','hippo','rhino']	// 리스트
>>> animal
['lion', 'hippo', 'rhino']
>>> nums = [1,2,3,4]	// 리스트

>>> vars = [1,3.14,'greg']		// 리스트 // C언어에서 struct와 비슷함
>>> vars
[1, 3.14, 'greg']

>>> a = [1,2,'a','b',[4,5,6]]	// 리스트에 자료형 상관없이 다 넣을 수 있음
>>> a[1]
2
>>> a[4]
[4, 5, 6]
>>> a[4][1]	// 리스트 안에 리스트 접근할 때
5
>>> a[4][2]
6
>>> a = [1,2,[3,4,[5,6]]]		// 리스트 안에 리스트, 2중 3중 더많이 가능
>>> a[2][2][1]
6

>>> a[-2]		// 획기적 indexing / 맨뒤-1부터 시작
2
>>> a[-1]
[3, 4, [5, 6]]
>>> a[-1][-1]
[5, 6]

>>> a = [1,2,'a','b',[4,5,6]]
>>> a[0:3]				// List Slicing리스트 슬라이싱 : 0이상3미만
[1, 2, 'a']
>>> del a[0]				// 변수 지워버림
>>> a
[2, 'a', 'b', [4, 5, 6]]

>>> a.append(7)		// append덧붙이다,추가하다 / 리스트 맨 뒤에 변수 추가
>>> a
[2, 'a', 'b', [4, 5, 6], 7]
>>> a.pop()			// 제일 마지막에 들어온, 추가된 변수 출력 후 없앰
7

		🇧🇷🇧🇷🇧🇷Queue큐 : 줄서기 FIFO FirstInFirstOut
		🇧🇷🇧🇷🇧🇷Stack스택 : 접시쌓기 LIFO LastInFirstOut
		a.append(7) 한 뒤에 a.pop() 하면 스택 구현함

>>> a
[2, 'a', 'b', [4, 5, 6]]
>>> print(a)
[2, 'a', 'b', [4, 5, 6]]
>>> a.insert(1,2)		// a[1] 자리에 2를 집어넣고 이후것들은 자리를 뒤로 미룸
>>> a
[2, 2, 'a', 'b', [4, 5, 6]]
>>> a.insert(3,'c')
>>> a
[2, 2, 'a', 'c', 'b', [4, 5, 6]]

>>> a.insert(0,9)
>>> a
[9, 2, 2, 'a', 'c', 'b', [4, 5, 6]]
>>> del a[0]
>>> a
[2, 2, 'a', 'c', 'b', [4, 5, 6]]

>>> a.remove('a')
>>> a
[2, 2, 'c', 'b', [4, 5, 6]]

>>> b = [3,5,1,2,7]
>>> b.sort()			// 정렬시킴, 원본이 정렬됨
>>> b
[1, 2, 3, 5, 7]

>>> b = [3,5,1,2,7]
>>> c = sorted(b)	// 원본은 그대로 두기 위해서, 정렬된 것을 다른 객체에 저장함
>>> c
[1, 2, 3, 5, 7]
>>> b
[3, 5, 1, 2, 7]

>>> c = b.sort()
>>> c
>>> c
>>> b
[1, 2, 3, 5, 7]



>>> a = [1,2,3]
>>> b = a
>>> a[1] = 5
>>> b[1]
5
```

- if 문, indentation으로 중괄호 기능, 주석, for 문
```
>>> a = 10
>>> if a == 10:
...     print("OK")
... 
OK
>>> exit()

#a = 13		#은 한줄주석, ‘’’은 구간주석
‘’’
if a==10 or a==12 :
    print("Yes, 10 or 12")
elif a == 13 :
    print("It's 13")
else :
    print("Neither")
'''


for i in range(0,10):			// 0이상 10미만 실행하라, 0부터9까지
    print("ㅇㅣㅂㅓㄴㅇㅛㅅㅗㄴㅡㄴ ",i)

li = [1,3,6,12,5]
for i in li:				// li리스트 처음부터 끝까지,,,그 다음은 다음실행에 따라서
    print(i)

lii = ['python is', ' easy to learn', ' however powerful']
for i in lii:
    print(i)

for i in ['python is', ' easy to learn', ' however powerful’] :	// 이것도 가능
	print(i)
```

- 이제 IDLE로 실행하면 편함. 지금까지 본걸로 기초적인 프로그램을 만들 수 있음
```
###FIZZBUZZ
num = int(input("<FIZZBUZZ>\nInput number : "))
for i in range(1,num+1):
    if i%15==0:
        print("FIZZBUZZ")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else :
        print(i)


import random
answer = random.randint(1,10)	// 1부터10포함까지
guess = int(input("Input number : “))	// input()은 무조건 string타입으로 입력받음…그래서 int()로 씌어줘서 변수 형태를 변경시켜줘야한다
if guess == answer :
    print("You Win")
else :
    print("You Lose, the answer is %d" % answer)


result = eval(input("Input number : "))
//eval()로 씌어주면 int()와 같이 변수 형태를 변경시켜주지만…eval()은 연산자가 들어가있는지 evaluate평가를 해서 3+5 라는 값을 입력받아도 8로 입력을 받아줌…하지만 int()로 씌우면 3+5 같은 경우 그냥 string형태로 받음…이런 차이가 있음 // num = eval(“3+5”)도 가능


print(type(result))	// result 변수의 타입을 출력

li = [i+3 for i in range(1,301) if I%2==0]	// ListComprehension
1부터 300까지 / i가 2의 배수이면 / 조건충족한 i로 li리스트 만듬

###REFACTORING NUMGUESS

import random

name = input("Input Name : ")
print("Hi " + name + ", Guess the Number!")
answer = random.randint(1,10)
cnt = 1
while 1:
    guess = int(input("Input number : "))
    if cnt == 10:
        print("Game Ended\nYou Lost All Your Chances")
        print("The answer was %d" % answer)
        break
    elif guess == answer:
        print("You got it in %d times" % cnt)
        break
    else:
        cnt = cnt+1


def anti_vowel(text):
    li = []
    new = []
    for i in text:
        li.append(i)
    for i in range(len(li)):
        if li[i] not in "aeiouAEIOU":
            new.append(li[i])
    return "".join(new)
text = str(raw_input("Input text : "))
print(anti_vowel(text))
```