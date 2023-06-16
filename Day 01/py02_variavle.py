# 변수
import sys 

number = 21000000000
value = sys.maxsize # sys.maxsize 파이썬 시스템에서 제공하는 최고 숫자(overflow 없음 걍 더해짐)

print(number)
print(value)
print(value+1) #가능 overflow 없음

value2 = 0o12  #8진수

print(value2)

value2 = 0xFF #16진수
print(value2) 
value2= 'Hello, python'
print(value2)

value2 = False
print(value2 == False)

# 사칙연산
print(14/2) #소수점 나누기
print(14 // 2) # 정수 나누기
print(2 ** 10) #승수 2의 10승
print(3 % 3) #3의 배수

