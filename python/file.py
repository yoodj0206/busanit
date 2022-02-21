#파일 열기
# f=open('python/새파일.txt', 'w') 
# f=open('python\\새파일.txt', 'w')

#파일 닫기
# f.close()

# f = open("새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("python/새파일.txt", 'a')    //작성되어 있는 내용 뒤로 작성된다.
# for i in range(11, 21):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("python/새파일.txt", 'w')    //작성되어 있는 내용을 삭제한 후 다시 작성된다.
# for i in range(21, 31):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("python/새파일.txt", 'w')
# for i in range(21, 31):
#     data = "%d번째 줄입니다." % i     //한줄로 적힌다.
#     f.write(data)
# f.close()

# f = open("python/새파일.txt", 'r')
# line=f.readline()
# print(line)
# f.close()

# f = open("python/새파일.txt", 'r')
# for i in range(1,11):
#     line=f.readline()
#     print(line, end='') 
# f.close()

# f = open("python/새파일.txt", 'r')
# while True:
#     line=f.readline()
#     if not line: break
#     print(line, end='')
# f.close()

# f = open("python/새파일.txt", 'r')
# lines=f.readlines()
# for line in lines:
#     line = line.strip()
#     print(line)
# f.close()

# f=open('새파일.txt', 'w')
# f.write('Life is to short, you need python')
# f.close()

# with open('foo.txt', 'w') as f:
#     f.write('Life is too short, you need python')

