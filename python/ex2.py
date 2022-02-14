# 01 다음 코드의 결과 값은 무엇일까?
a='Life is too short, you need python'

if 'wife' in a: print('wife')                           #만약 wife가 있다면 출력해라                => 거짓
elif 'python' in a and 'you' not in a: print('python')  #만약 python이 있고, you가 없으면 출력해라  => 거짓
elif 'shirt' not in a: print('shirt')                   #만약 shirt가 없다면 출력해라               => 진실
elif 'need' in a: print('need')                         #만약 need가 있다면 출력해라                => 진실
else: print('none')                                     #그렇지 않다면 none을 출력해라
#3번째 가정인 'shirt'가 진실이기 때문에 출력은 'shirt'만이 출력된다.

# 02 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
result=0
i=1
while i < 1000:
    if i%3==0:
        result+=i
    i+=1
print(result)

# 03 whil문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
i=0
while True:
    i +=1
    if i >5: break
    print('*'*i)

# 04 for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for i in range(1,101):
    print(i, end=' ')
print()

# 05 A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
#    [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#    for문을 사용하여 A 학급의 평균 점수를 구해 보자.
A=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in A:
    total += score
average=total/len(A)
print(average)

# 06 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
#    위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
number=[1, 2, 3, 4, 5]
result=[]
for n in number:
    if n % 2 == 1:
        result.append(n*2)
print(result)

number=[1,2,3,4,5]
result=[(n*2) for n in number if n%2==1]
print(result)
