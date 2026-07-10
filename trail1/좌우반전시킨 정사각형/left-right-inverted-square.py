n = int(input())

for i in range(1,n+1): 
    for j in range(n,0,-1):#좌우반전
        print(i*j, end=" ")
    print()