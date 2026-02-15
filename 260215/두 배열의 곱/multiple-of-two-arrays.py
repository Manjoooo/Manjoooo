arr1 = [list(map(int,input().split())) for _ in range(3)]
#첫번째, 두번째 2차원 배열 입력
input()

arr2 = [list(map(int,input().split())) for _ in range(3)]

arr3 =[[0 for _ in range(3)] for _ in range(3)]
#2차원 배열을 구현 

for i in range(3):
    for j in range(3):
        arr3[i][j] = arr1[i][j] * arr2[i][j]
    
#두 배열의 곱을 새로운 배열에 담음

for a in arr3:
    for b in a:
        print(b, end= " ")
    print()

#요소로 표현해도 되는 부분이랑. 
#for i in range(3):        
#    for j in range(3):    
#        print(arr_3[i][j], end=" ")
#    print()