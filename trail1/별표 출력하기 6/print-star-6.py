n = int(input())

# 위쪽 절반 출력
for i in range(n):
    # 공백 출력
    for j in range(i):
        print(" ", end=" ")
    # 별 출력
    for j in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()

# 아래쪽 절반 출력
for i in range(1, n):
    # 공백 출력
    for j in range(n - 1 - i):
        print(" ", end=" ")
    # 별 출력
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()