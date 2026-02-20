N = int(input())

for i in range(N):
    for j in range(N):
        if j % 2 == 0:
            print(i+1, end="")
        else:
            print(N-i, end="")
    print()


#0부터 시작
#규칙을 찾아야함. 