from turtle import *
from math import *

SCALE = 10
#데이터의 개수가 30개일 때
list_x = [x* 0.1 for x in range(1, 301)]

def magnify(x, y):
    _x = x*SCALE
    _y = y*SCALE
    return _x, _y

tracer(False)

#x축 선을 긋는다 : -10 ~ 10
up()
goto(-30 * SCALE, 0)
down()
forward(30 * 2 * SCALE)
write('n')

#y축 선을 긋는다 : -10 ~ 10
up()
goto(0, -30 * SCALE)
left(90)
down()
forward(30 * 2 * SCALE)
write('T(n)')

# O(n^2)
for x in list_x:
    y = x**2
    up()
    _x, _y = magnify(x, y)
    goto(_x, _y)
    dot(4, 'red')

goto(40, 200)
write("O(n^2)", font=("Arial", 12, "bold"))


# O(n*logn)
for x in list_x:
    y = x*log(x, 10)
    up()
    _x, _y = magnify(x, y)
    goto(_x, _y)
    dot(3, 'blue')

goto(140, 270)
write("O(n*logn)", font=("Arial", 12, "bold"))



#O(n)
for x in list_x:
    y = x
    up()
    _x, _y = magnify(x, y)
    goto(_x, _y)
    dot(2, 'green')

goto(205, 180)
write("O(n)", font=("Arial", 8, "normal"))


#O(logn)
for x in list_x:
    y = log(x, 10)
    up()
    _x, _y = magnify(x, y)
    goto(_x, _y)
    dot(2, 'purple')

goto(300, 20)
write("O(logn)", font=("Arial", 8, "normal"))

#O(1)

for x in list_x:
    y = 1
    up()
    _x, _y = magnify(x, y)
    goto(_x, _y)
    dot(2, "orange")

goto(310, 0)
write("O(1)", font=("Arial", 8, "normal"))


    


