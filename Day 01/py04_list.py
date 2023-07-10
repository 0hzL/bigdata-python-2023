# 리스트
import datetime as dt

value = dt.datetime.now()
lists = [1,2,3,4,[5,6,7],True,'Hello', value]

print(lists)
print(lists[-2])
print(lists[-1]) # java=null
print('**********************')

print(lists[4][1]) # 6
print(lists[-2][-1]) # o

print(lists[:4]) # 두번째값은 마지막 찾고싶은 인덱스 + 1 (파이썬 종특)

print('**********************')

#리스트 연산
a = [1,2,3]
b = [4,6,8]
print(a+b)
print(a*2)

a[2] = False #2번 인덱스에 False를 할당
print(a)

del b[2] #2번 인덱스를 지워라
print(b)

print('**********************')
#리스트 함수(문자열 함수 만큼 중요)
c = [3,6,9]
c.append(12) #리스트 마지막에 추가
print(c)

print('**********************')
d = [6,4,9,3,2,1]
d.sort()
print(d)

print('**********************')
e = [3,4,6,2,5]
e.reverse() #순서를 뒤집는 것
print(e)
print('**********************')
e.sort(reverse=True) # 정렬(내림차순)
print(e)
e.insert(2,5.5) # 2번 인덱스에 5.5 입력
print(e)
print(e.index(5.5)) #값 찾기wjswjdrnr^61


print('**********************')
e.append(6)
print(e)
e.remove(6)
print(e)
e.remove(6)
print(e)