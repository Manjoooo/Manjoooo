n = int(input())

for i in range(n):
    inp = input()
    arr = inp.split()
    a,b = int(arr[0]), int(arr[1])

    ant = 0

    for j in range(a,b+1):
        if j % 2 == 0:
            ant += j
    print(ant)
#일단 n번째 줄까지 