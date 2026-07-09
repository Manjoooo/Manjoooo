n = int(input())

# 1. 위쪽 절반 출력 (1부터 n까지)
for i in range(1, n + 1):
    if i % 2 != 0:
        print("* " * (n - (i // 2)))
    else:
        print("* " * (i // 2))

# 2. 아래쪽 절반 출력 (n부터 1까지 거꾸로 역방향 루프)
for i in range(n, 0, -1):
    if i % 2 != 0:
        print("* " * (n - (i // 2)))
    else:
        print("* " * (i // 2))