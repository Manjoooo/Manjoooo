N = int(input())

for i in range(N):
    for j in range(N):
        if i % 2 == 0:
            print(j+1, end="")
        else:
            print(N-j, end="")
    print()

#4행에 숫자 4까지하니까 for문이 이중중첩으로 와야함. 
#마지막 PRINT()는 줄바뀜