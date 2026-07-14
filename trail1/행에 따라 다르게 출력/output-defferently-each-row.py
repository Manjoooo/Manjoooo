n = int(input())

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            # 홀수 번째 줄: 앞선 세트들(3*n)만큼 건너뛰고 1씩 증가 (+j)
            print(1 + (i // 2) * 3 * n + j, end=" ")
        else:
            # 짝수 번째 줄: 직전 줄 시작점 기준 n+1만큼 더한 곳에서 2씩 증가 (+2*j)
            print(1 + (i // 2) * 3 * n + n + 1 + 2 * j, end=" ")
    print()