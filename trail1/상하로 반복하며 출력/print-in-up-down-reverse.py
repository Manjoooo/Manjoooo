n = int(input())

for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            # 짝수 번째 열은 위에서 아래로 (1, 2, 3, 4...)
            print(i + 1, end="")
        else:
            # 홀수 번째 열은 아래에서 위로 (4, 3, 2, 1...)
            print(n - i, end="")
    print()  # 한 줄 처리가 끝나면 줄바꿈