# # 논리값은 True, False(첫글자는 대문자, 나머지는 소문자)
# money = True
# # if <조건문>:
# if money:
#     print('택시를 타고 가라')
# else:
#     print('걸어 가라')

# ▶비교 연산자

# money = 2000
# if money >= 3000:
#     print ('택시를 타고 가라')
# else:
#     print('걸어가라')

# money = 2000
# card = True
# if money >= 3000 or card:
#     print('택시를 타고 가라')
# else:
#     print('걸어가라')

# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket:
#     print('택시를 타고 가라')
# else:
#     print('걸어가라')

# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket:
#     pass
# else:
#     print('카드를 꺼내라')


#elif문 

# pocket = ['paper', 'cellphone', 'money']
# if 'card' in pocket:
#     print('택시를 타고가라')
# else:
#     if 'money' in pocket:
#         print('돈을 꺼내라')
#     else:
#         print('걸어가라')

# pocket = ['paper', 'cellphone']
# card = True
# if 'money' in pocket:
#     print('택시를 타고 가라')
# elif card:
#     print('택시를 타고 가라')
# else:
#     print('걸어가라')
    
# ▶if문을 한 줄로 작성하기(한줄일 경우에만)

# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket:
#     pass
# else:
#     print('카드를 써라')
    
# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket: pass
# else: print('카드를 써라')

# ▶조건부 서식
# score = 70
# if score >= 60:
#     message = 'success'
# else:
#     message = 'failure'
# print(message)

# #         참인 경우 if 조건문      else 거짓인 경우
# message = 'success' if score >= 60 else 'failure'
# print(message)

# pocket = ['paper', 'cellphone', 'money']
# message = '택시를 타고 가라' if 'money' in pocket else '걸어가라'
# print(message)