cnt3, cnt5 = 0, 0

for _ in range(10):
    a = int(input())

    if a % 3 == 0:
        cnt3 += 1
    if a % 5 == 0:
        cnt5 += 1

print(cnt3,cnt5)

#range는 0부터 9까지니까 10개의 수는 맞음
#그리고 그 안에 입력하고 그 값이 a로 정의되도 상관없음. 
#10개의 서로 달느 숫자를 넣는 거기 때문에 if 문 안에 있어야함. 10번 반복이기 때문에
