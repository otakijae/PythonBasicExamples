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


## Python version 확인 및 잡다한 기능
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

## Print something / Interpreter Language
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

## 객체 생성 및 할당 쉽게(객체 할당하는 것을 스티커를 붙여준다고 생각하면 쉽게 이해됨)
```
>>> a=10		// 상수 객체의 공간을 만들어서 a라는 스티커를 붙여 이름을 정함
>>> b=10		// a의 값과 같은 값을 가지고 있어서, 같은 객체의 공간에 b라는 스티커를 붙여 다른 이름을 정해줌
>>> print(id(a), ' ', id(b))		
4297624224   4297624224
>>> a = 15
>>> print(id(a), ' ', id(b))
4297624384   4297624224	// a의 값이 변경돼서, 다른 주소가 출력이 됨
```

## String in Python
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

## Python의 신기하고 유용한 메소드들
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

## Python 2.7.10은 맥에서 기본 내장된 Python이기 때문에 다운받은 Python2.7이나 Python3.6을 간단하게 python명령으로 실행시키려면 아래와 같이 하면 된다. 나중에 Python 가상 개발 환경을 세팅을 해야되는데 일단은 간단하게 이렇게 실행하면 쉽다.
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

## List [ ]
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

		🇧🇷🇧🇷🇧🇷 Queue큐 : 줄서기 FIFO FirstInFirstOut
		🇧🇷🇧🇷🇧🇷 Stack스택 : 접시쌓기 LIFO LastInFirstOut
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

## if 문, indentation으로 중괄호 기능, 주석, for 문
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

## 이제 IDLE로 실행하면 편함. 지금까지 본걸로 기초적인 프로그램을 만들 수 있음
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

## Function
```
def one_dim_func(x):
    y = 3*x+2
    return y

def two_dim_func(x):
    y = 3*(x**2)-5
    return y

def func3(x,y):
    z = 3*x + y
    return z
```

## Call by Assignment…immutable인 상수 객체는 참조 안 함
## 처음에는 Reference 참조를 받는 것을 원칙으로 하지만, immutable객체를 만나 변경을 시도하면 참조를 할 수 없다고 판단함
```
def func333(a,b):			// Call by Assignment in Python
    z = a+b
    a,b = b,a
    print("a = {0}, b = {1} in func333 \n" .format(a,b))	// 이런 방법도 있음 {}안 숫자 순서 맞게 포맷 순서대로 넣음
    return z

a = 3
b = 5
z = func333(a,b)
print("a = {}, b = {} \n".format(a,b))		// 포맷순서대로 넣음
print(z)

def func(a, b):
	    print("a : {} b : {} before change in function".format(id(a), id(b)))
	    a = 15
	    print("a : {} b : {} after change in function".format(id(a), id(b)))
a = 10
b = 5
print("a : {} b : {} before function".format(id(a), id(b)))
func(a, b)
print("a : {} b : {} after function".format(id(a), id(b)))
```

## Call by Assignment…mutable인 List객체는 참조를 함
## 처음에는 Reference 참조를 받는 것을 원칙으로 하지만, immutable객체를 만나 변경을 시도하면 참조를 할 수 없다고 판단함
```
b = [1,2,3]				// Call by Assignment in Python
def Func(a):
    a[1] = 7				// List는 변경가능해서 밖의 b리스트를 참조해서 변경시킴
    a = [11,12,13]	//근데 리스트 전체를 아예 새로 할당을 하려고 하면 Python 스스로(Call by Assignment) 밖의 b를 참조할 수 없다고 판단하고, 상관없는 새로운 a리스트를 생성함
    return a		// 이렇게 따로 반환하는 게 없으면 새로 할당한 a리스트는 함수가 끝나면 사라짐

c=Func(b)		//이렇게 하면 return값 a = [11,12,13]을 출력할 수 있음
print(c)
Func(b)			//이렇게 하면 변경된 b리스트 [1,7,3]을 출력할 수 있음
print(b)

def func(a):
	   print("a : " + str(id(a)) + " before trying change in func")
	   a[1] = 7
	   print("a : " + str(id(a)) + " after trying change in func")
	   a = [11, 12 ,13]
	   print("a : " + str(id(a)) + " after allocating in func")	
li = [1, 2, 3]
print("li : " + str(id(li)) + " before functiuon")
func(li)
print("li : " + str(id(li)) + " after function")
```

## LEAP YEAR 윤년 계산
```
def is_leapyear(y):
    leap = False
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        leap = True
    return leap

def is_leap(a):
    if a%4 == 0 and a%100 == 0 :
        return False
    elif a%4 == 0 and a%400 == 0 :
        return True
    elif a%4 == 0 :
        return True
    else :
        return False
year = int(input("Input year : "))
bleap = is_leap(year)
print(bleap)
```

## Dictionary	// OpenAddressing&ClosedAddressing
```
dic = {1:['a','b','c'], 2:34, 3:(1,2,3)}
print(dic)

dic1 = {key1 : value1, key2 : value2, key3 : value3, .....}	// 키값은 고유, 중복불가, 혹시라도 중복될 시 하나는 무조건 무시함, 그래서 그렇게 안 하면 됨

Key 값 하나당, 여러 value값들을 이어붙임.

dic1 = { 'name' : “신재혁” , "age" : 35, "weight" : 70.5}

dic1[“money”] = 5000		// 새롭게 Dictionary에 추가시킴…어차피 순서가 없어서 아무곳에 추가됨…키값으로 접근하면 되니까 상관없음
dic1[“language”] = [‘c’, ‘c++’, ‘python’]	// language키값에 리스트로 값 추가시킴
dic1[“language”][1]			// 이런식으로 접근하면 됨
del dic1[‘name’]			// 키값을 통해서 지울 수 있음

dic1.keys()			// 키값들만 반환…리스트가 아닌 객체로 반환…순회가능해서 출력가능
dic1.value()			// value값들만 반환…리스트가 아닌 객체로 반환…순회가능해서 출력가능
dic1.items()			// 키값이랑 value값을 튜플로 묶어서 반환…리스트가 아닌 객체로 반환…순회가능해서 출력가능
dic1[“KEY값”]			이상한 키값 입력 시 ERROR
dic1.get(“KEY값”)		이상한 키값 입력 시 None 반환
```

## Set		// 집합…거의 안 쓸 수 도 있음…
```
s = set( [1,2,3,4] )		// s 출력하면 { } 안에 나타나는데, 리스트나 튜플형태가 아니라는 것임
s.add(5)				// 순서 없이 들어감
s.update( [6,7,8] )		// 여러개 넣을 때
s.remove(5)			// 그냥 지움

s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6])

s1 & s2				//교집합
s1.intersection(s2)

s1 | s2				//합집합
s1.union(s2)

s1 - s2				//차집합
s1.difference(s2)
```

## Write txt file
```
f = open(“test.txt”, “wt”)
		// wt : write text file		// 다시 실행하면 기존에 있던 파일 지우고 다시 씀
		// wb : write binary file
		// rt : read text file
		// rb : read binary file
		// at : add text file		// 다시 실행해도 기존에 있던 파일에 추가하는 형식으로 씀
		// ab : add binary file
f.close()					// 항상 열여줬으면 닫아야 하고, 안 닫으면 계속 파일이 실행되므로
```
## Append txt file
```
f = open("test.txt", "at")
for i in range(4):					// range(4)만 하면 0부터 3까지란 뜻
    data = input("Input string : ")		
    slen = len(data)					// 그냥 파일에 넣으면 엔터 없이 쭉 이어서 넣어서
    data2 = data + '\n'	// 엔터\n을 추가시키기 위한 작업…string자체를 변경시킬수 없기 때문에 따로 뉴라인을 추가시켜줌
    f.write(data2)
f.close()
```
## Read txt file / read()
```
f = open(“test.txt”, “rt”)	// 이렇게만 해서 파일을 받으면 한줄한줄 받는게 아니라 텍스트 파일 안에 있는 것 전체를 하나의 스트링 객체로 받음
data = f.read()
print(data)
f.close()
```
## Read txt file / readline()
```
f = open("test.txt", "rt")	// 그래서 한줄한줄씩 받으려면 이렇게 사용
for i in range(4):		// 줄이 몇줄이 있는지 범위를 알때만 이렇게 사용하고
    data = f.readline()
    print(data)
f.close()
```
## Read txt file / readline() until End of file
```
f = open("test.txt", "rt")	// 그래서 결국엔 이렇게 텍스트파일 마지막까지 가서 읽을 라인이 없을 때까지 입력을 받게 설정을 해야함
while 1:
    data = f.readline()
    if not data:			// 텍스트 파일에 더이상 받을 데이터가 없으면 while루프를 종료하라
        break
    else:
        print(data)
f.close()
```
## Read txt file / readlines()
```
f = open("test.txt", "rt")	
str_list = f.readlines()	// 텍스트 파일에 있는 한줄한줄의 데이터를 리스트로 불러서 저장
real_list = []			
print(str_list)			// 텍스트 파일 데이터 입력 받을때, 가독성을 위해 \n을 붙였기 때문에 출력하면 “데이터\n” 이런식으로 리스트에 추가된 것을 볼 수 있음
for st in str_list:		
    slen = len(st)-1		// 그래서 \n제외한 데이터를 새로운 리스트에 저장을 하기위해
    s = st[0:slen]		// 슬라이싱 사용 … 0에서 slen-1까지
    real_list.append(s)
    print(s)
f.close()
```


## Procedural Programming Data Analysis / 기초적인 절차지향 데이터 분석 예제 프로그램
- 먼저 실행하면 binary 파일 생성함
```
import pickle

f = open("class_A.bin", "wb")

data = {"JaeHyuk Shin":100}
pickle.dump(data,f)			// f.write(data)와 같은 건데 pickle을 사용해서 이렇게 사용

data = {"Wayne Rooney":78}
pickle.dump(data,f)

data = {"Paul Pogba":80}
pickle.dump(data,f)

data = {"Eden Hazard":95}
pickle.dump(data,f)

data = {"Mesut Ozil":100}
pickle.dump(data,f)

data = {"Harry Kane":100}
pickle.dump(data,f)

f.close()
```
- read binary file
```
import pickle
f = open("class_A.bin", "rb")
items = []
while 1:
    try :
        data = pickle.load(f)	// f.read(data)와 같은 건데 pickle을 사용해서 이렇게 사용
    except EOFError :
        break
    items.append(data)		

🇬🇹🇬🇹🇬🇹pickle을 import했을 시 pickle.load(f)를 하면,,,f.read(data)했을 때와 다르게
🇬🇹🇬🇹🇬🇹마지막에 읽을 데이터가 없으면 None을 반환하는게 아니라 Error를 출력을 함
🇬🇹🇬🇹🇬🇹그래서 try:except 구문으로 데이터 입력을 끝까지 받아야함

for i in items:			// Dictionary형태로 저장된 데이터이기 때문에
    key = list(i.keys())	// i는 items에서 가져온 Dictionary형태의 초기데이터,,,그래서 Dictionary에서 키값을 가져와 key에 저장함
    print(i[key[0]])		// i는 Dictionary이름이라고 생각하면 됨
f.close()
```
- binary 파일 데이터 분석
```
import pickle
import math

def average(scores):
    sum = 0
    for i in scores:
        sum+=i
    return sum / len(scores)

### 분산
#그 확률변수가 기댓값으로부터 얼마나 떨어진 곳에 분포하는지를 가늠하는 숫자
#기댓값은 확률변수의 위치를 나타내고 분산은 그것이 얼마나 넓게 퍼져 있는지를 나타낸다
#분산보다는 분산의 제곱근인 표준편차가 더 자주 사용된다
def variance(scores,avg):
    variance_sum = 0
    for i in scores:
        variance_sum += ((avg-i)**2)
    return variance_sum/len(scores)

def evaluateClass(avg, std_dev):
    if avg<50 and std_dev>20:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avg>50 and std_dev>20:
        print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
    elif avg<50 and std_dev<20:
        print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
    elif avg>50 and std_dev<20:
        print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")

f = open("class_A.bin", "rb")

items = []      // items라는 리스트 안에 Dictionary형태의 데이터를 저장할 예정

while 1:
    try :
        data = pickle.load(f)
    except EOFError :
        break
    items.append(data)

scores = []

#items리스트 안에  Dictionary형태의 데이터가 있으니까 for문으로 하나씩 빼와야함
###목적은 scores라는 리스트 안에 items의 Dictionary들의 value값들을 다 넣는 것
for i in items:
    keys = list(i.keys())
    for j in keys:
        scores.append( i[j] )

avg = average(scores)
variance = round(variance(scores, avg), 2)
standard_deviation = round(math.sqrt(variance), 2)

print('*' * 50)
print("A반 성적 분석 결과")
print('*' * 50)
print("A반의 평균은 {0}점이고 분산은 {1}이며, 따라서 표준편차는 {2}이다".format(avg, variance, standard_deviation))
print('*' * 50)
print("A반 종합 평가")
print('*' * 50)
evaluateClass(avg, standard_deviation)

f.close()
```