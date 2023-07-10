# 문제 1
jumin = input('주민등록번호(- 포함 입력) : ').split('-')
print(jumin[1][:1])
if(jumin[1][:1] == '1' or jumin[1][:1] == '3' or jumin[1][:1] == '5'):
    print('남성 입니다')
elif(jumin[1][:1] == '2' or jumin[1][:1] == '4' or jumin[1][:1] == '6'):
    print('여성 입니다')
else:
    print('주민등록번호를 확인해주세요')

#문제 2
weekday = input('요일을 입력하세요(ex: mon) : ').upper()
if(weekday == 'MON'):
    print('월요일')
elif(weekday == 'TUE'):
    print('화요일')
elif(weekday == 'WED'):
    print('수요일')
elif(weekday == 'TUR'):
    print('목요일')
elif(weekday == 'FRI'):
    print('금요일')
elif(weekday == 'SAT'):
    print('토요일')
elif(weekday == 'SUN'):
    print('일요일')



#문제 3
age = int(input('나이를 입력하세요 :'))
if(age < 19 ):
    print('애들은 가라')
elif(age >=19):
    print('어서오십시오. 손님~!!')

#문제4

filename = './result.txt'
f = open(filename, mode='wt', encoding='utf-8') 

num = 1
while num <= 10000:
    if( num % 3 == 0 or num % 5 == 0):
        f.write(str(num) + '\n')
    num += 1

f.close() 
print(f'{filename} 이(가) 생성되었습니다')


#문제 5
from datetime import datetime
now = datetime.now()
formattedDate = now.strftime('%Y\%m-%d %H*%M%%%S')
print(formattedDate)