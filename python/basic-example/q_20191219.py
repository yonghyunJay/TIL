'''
# 문제 1.
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
ex) python py_quest.py 실행 후 나타나는 입력란에 
    ABCDEFG 입력시 
    A G 출력
'''
str = input('문자를 입력하세요: ')
# 아래에 코드를 작성해 주세요.
# print(str[0], str[len(str)-1])
print(str[0], str[-1])

'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
ex) python py_quest.py 실행 후 나타나는 입력란에
    2 입력시 
    0
    1
    2 출력
'''
numbers = int(input('숫자를 입력하세요: '))
# 아래에 코드를 작성해 주세요.
# for count in list(range(numbers + 1)):
#     print(count)
for count in range(numbers):
    print(count)
'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
ex) python py_quest.py 실행 후 나타나는 입력란에
    2 입력시 
    짝수 출력
'''
number = int(input('숫자를 입력하세요: '))
# # 아래에 코드를 작성해 주세요.
# if number % 2 == 0 :
#     print('짝수')
# else :
#     print('홀수')
if number % 2 :
    print('홀수')
else :
    print('짝수')