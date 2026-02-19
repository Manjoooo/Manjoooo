matrix = [list(map(int, input().split())) for _ in range(4)]

ans = 0 #누적합계일때는 밖에다가 정의 
#i문 행마다 저장해야할때는 안에다가 정의 
for i in range(4):

    for j in range(4):
        if matrix[i][j] % 5 == 0:
            ans += 1


print(ans)