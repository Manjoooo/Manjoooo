n = int(input())

for i in range(n): #loop가 돌아갈때마다 i가 증가 
    for j in range(n-i): # 시작하자마자 *을 찍는다는 의미 
        print("*", end =" ")
    print() # 다음줄로 넘어가게 하는 역할 

