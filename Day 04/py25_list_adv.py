# 리스트 고급사용
# 1. 1 ~ 1000 까지 사이의 3의 배수값 리스트 ( 편한 방법 )
list_3rd = []
for n in range(1, 1000+1):
    if n % 3 == 0: #3의 배수이면
        list_3rd.append(n)

print(list_3rd)
print("**********************")

#2. 1~1000 까지 사이의 ( 굳이 )
list_3rd_2 = [n for n in range(3,1000+1,3)]
print(list_3rd_2)

##
print([2 * x for x in range(1,10+1)])

# 3. 3의 배수 구하기
print([3 * x for x in range(1,333+1)])

# 4. 1~1000까지 사이의 3의 배수값 리스트
list_3rd = []
for n in range(1, 1000+1):
    if n % 3 == 0: #3의 배수이면
        list_3rd.append(n)

print([x for x in range(1,101) if x % 3 == 0]) # for문 if문 전부처리

# zip하고 유사함
print([(x,y) for x in ['광어','고등어','연어'] for y in ['한돈','한우','한계']])