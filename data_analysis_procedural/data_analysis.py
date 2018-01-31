import pickle
import math

def average(scores):
    sum = 0
    for i in scores:
        sum+=i
    return sum / len(scores)

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

items = []      #Dictionary in List

while 1:
    try :
        data = pickle.load(f)
    except EOFError :
        break
    items.append(data)



scores = []
#items리스트 안에  Dictionary가 있으니까 for문으로 하나씩 빼와야함
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
