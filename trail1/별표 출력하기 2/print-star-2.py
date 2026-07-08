n = int(input())

for i in range(n,0,-1): # 한개씩 줄어드는것
    for j in range(i):
        print("*", end=" ")
    print() #줄바꿈