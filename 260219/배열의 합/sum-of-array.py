matrix = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):
    ans = 0
    for j in range(4):
        ans += matrix[i][j]
    print(ans)
#i는 행이기때문에 줄 전체에 합을 구해줄 코드임. 모든 행에 해당하는 값들을 더함.