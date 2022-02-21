# def 함수명(매개변수):
#     <수행할 문장1>
#     <수행할 문장2>
    
# def add(a, b):    //add라는 함수를 만듬
#     return a+b    //a와 b를 더하고, 그 값을 돌려준다.
# print(add(5,3))   //5와 3을 함수에 적용하여 나온 값을 보여준다.

# def add(a, b):
#     return a+b
# x = 3
# y = 4
# c = add(x,y)
# print(c)

# def say():
#     return 'Hi'
# a=say()
# print(a)
# //or
# def say():
#     print('Hi')
# say()

# def add(a,b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a+b))
# a=add(5,3)
# print(a)

# //매개변수 지정하여 호출하기
# def add(a, b):
#     return a+b
# result=add(5, 3)
# print(result)
# result=add(a=3, b=7)
# print(result)
# result=add(b=5, a=3)
# print(result)

# 여러 개의 입력값을 받는 함수 만들기
# args=[1,2,3,4,5]
# for i in args:
#     print(i)

# args=[1,2,3,4,5]
# result=0
# for i in args:
#     result+=i
# print(result)

# argument : 인자 / Parameter : 매개변수
# def add_many(*args):        # args : 인자
#     result=0
#     for i in args:
#         result+=i
#     return result
# result=add_many(1,2,3)
# print(result)
# result=add_many(1,2,3,4,5,6,7,8,9,10)
# print(result)

# def add_mul(choice, *args):
#     if choice == 'add':
#         result=0
#         for i in args:
#             result+=i
#     elif choice == 'mul':
#         result = 1
#         for i in args:
#             result*=i
#     return result
# result = add_mul('add', 1,2,3,4,5)
# print(result)
# result = add_mul('mul', 1,2,3,4,5)
# print(result)

#함수의 결과값은 언제나 하나이다.
# def add_and_mul(a,b):
#     return a+b, a*b
# result=add_and_mul(3,4)
# print(result)
# print(type(result))

# def add_and_mul(a,b):
#     return a+b, a*b
# result1, result2=add_and_mul(3,4)
# print(result1, result2)
# print(type(result1))
# print(type(result2))

# def say_myself(name, old, man=True): 
#     print("나의 이름은 %s 입니다." % name) 
#     print("나이는 %d살입니다." % old) 
#     if man: 
#         print("남자입니다.")
#     else: 
#         print("여자입니다.")
# print(say_myself('홍길동', 23))
# print(say_myself('홍길동', 23, True))
# print(say_myself('박응선', 27, False))

# def say_myself(name, man=True, old): 
#     print("나의 이름은 %s 입니다." % name) 
#     print("나이는 %d살입니다." % old) 
#     if man: 
#         print("남자입니다.") 
#     else: 
#         print("여자입니다.")
# print(say_myself('홍길동', 23)) //초깃값을 설정해 놓은 매개변수 뒤에 초깃값을 설정해 놓지 않은 매개변수는 사용할 수 없다는 뜻

#함수 안에서 선언한 변수의 효력 범위
# a = 1
# def vartest(a):
#     a = a +1
#     print('함수안의 a의 값 %d' % a)
# vartest(a)
# print('함수밖의 a의 값 %d' % a)

#
# a=1                 #전역변수
# def vartest(a):     #--
#     a+=1            # | 지역변수
#     return a        #--
# a=vartest(a)
# print(a)

# a = 1 
# def vartest(): 
#     global a 
#     a = a+1

# vartest() 
# print(a)
