n = int(input())

cnt = 0

for i in range(1, n+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    cnt += 1

#c친근한 수는 2,3,5로 나누어 떨어지는 수
#친근하지 않은 수의 개수를 출력하기 때문에 친근한 수는 continue 적용
print(cnt)