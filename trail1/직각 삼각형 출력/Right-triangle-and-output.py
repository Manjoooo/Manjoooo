n = int(input())

for i in range(n): 
    for j in range(2*i+1): # 별을 range 값만큼 출력
        print("*", end="")
    print() #줄바꿈