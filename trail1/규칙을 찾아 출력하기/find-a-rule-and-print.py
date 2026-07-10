# 변수 선언 및 입력
n = int(input())

for i in range(n):
    for j in range(n):
        # 첫 줄과 마지막 줄은 무조건 가득 채우기
        if i == 0 or i == n - 1:
            print("* ", end="")
        else:
            # 중간 줄에서는 맨 오른쪽 벽(j == n - 1)이거나,
            # 왼쪽에서부터 i번째 칸까지만 별을 채웁니다 (j <= i)
            if j == n - 1 or j < i:
                print("* ", end="")
            else:
                print("  ", end="")
    print()
