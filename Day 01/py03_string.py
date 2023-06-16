# 문자열

value = "Hello World"
print(value)
print('Hello World')

print('내 최애는 "전정국" 입니다')

value='''
안녕하세요.
저는 프로그래머입니다.
프로그래밍 열심히할게용
''' #여러줄 문장만들기

print(value)

'''
얘는 여러줄 주석으로 대체합니다
파이썬에는 여러줄 주석이 없어서 여러줄 문자열로 이역할을 대신합니당
'''

print('hello' + 'world!')
# print('hello'+ 4) # 예외 문자열 + 숫자 안됨
# print('hello'* 'world') # 예외 문자열 *문자열 안됨
print('hello' * 4)  

print(len('Life is too short')) # 문자열 길이 공백포함
print(len('최애의아이 9화봐야하는데')) # 문자열 길이 공백포함

origin = 'Life is short, You need Python'
print(origin[13])
print(origin[0]+ origin[16]+origin[19]+
      origin[20]+origin[0].lower() + origin[15].lower())
print(origin[:4]) #뒤의값은 인덱스값+1
print(origin[8:13])


print(origin[15:]) # index 15부터 끝까지
print(origin[15:-7]) # 음수는 뒤에서부터 인덱스 -1부터 시작

print('I ate %s apples' % ('three')) # %s string formating 문자열
print('I ate %d apples' % (3)) # %d integer formating 정수

print('pi is %f' % 3.14159265359) # %f floating-point formating 부동소수
print('pi is %10.2f' % 3.14159265359)

# 날짜 문자열 포맷팅
import datetime as dt

curr_dt = dt.datetime.now()
print(curr_dt)
print('오늘 날짜는 %s 입니다' % curr_dt.strftime('%Y년 %m월 %d일'))

#최신 포맷팅
apple_num = 3
print(f'I ate {apple_num} apples')
fmt_dt = curr_dt.strftime('%Y년 %m월 %d일')
print(f'오늘의 날짜는 {fmt_dt}입니다')

# 문자열 함수
# Life is short, You need Python
print(origin.count('o')) # 문자 묹자열의 개수
print(origin.find('Python')) # 문자 문자열 찾는 시작 인덱스 -1 없음

print('/'.join(origin)) # 문자 문자열 join에 있는 문자열이랑 하나식 합치는 함수
print(origin.upper()) # 전부 대문자
print(origin.lower()) # 전부 소문자
print(origin.capitalize()) # 문자열의 첫번째 단어만 대문자로
print(origin.title()) #단어의 첫번째 글자만 대문자로

#공백지우기
print('start'+'    Hello    '+'up') #기본
print('start'+'    Hello    '.lstrip()+'up') # 왼쪽 공백지우기
print('start'+'    Hello    '.rstrip()+'up') # 오른쪽 공백지우기
print('start'+'    Hello    '.strip()+'up') # 양쪽 공백지우기

result = origin.split(' ')
print(result)