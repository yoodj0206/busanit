#Q1
jumsu = [80, 75, 55]
avg = (sum(jumsu)/3)
print(f'평균은 {avg}입니다.')
# total = 0
# for i in jumsu:
#     total = total + i
#     # total += i
# avg = total / len(jumsu)
# print(f'평균은 {avg}입니다.')

#Q2
print(13 % 2)
# su = int(input('숫자를 입력하세요.'))
# if su % 2 == 0:
#     print('짝수입니다.')
# else:
#     print('홀수입니다.')

#Q3
pin = '881120-1068234'
year = pin[0:2]
month = pin[2:4]
day = pin[4:6]
num = pin[7:]
print('year =',year)
print('month =',month)
print('day =',day)
print('num =',num)
# ymd = pin[:6]
# num = pin[7:]
# print(ymd)
# print(num)


#Q4
pin = "881120-1068234"
print(pin[7])
# print(pin[-7])
# if pin[7] == "1":
#     print('남자')
# else:
#     print('여자')
    
#Q5
a = 'a:b:c:d'
b = a.replace(':', '#')
print(b)

#Q6
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#Q7
a = ['life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

#Q8
a = (1,2,3)
a = a + (4,)
print(a)


#9
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python'
a[250] = 'python'

#10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

#12
a = b= [1,2,3]
a[1] = 4
print(b)
