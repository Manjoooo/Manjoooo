N,M = tuple(map(int,input().split()))
#데이터가 변하지 않음을 강조하고 싶을 때 tuple을 사용하지만 안 써도 상관없음
arr1 =[list(map(int, input().split())) for _ in range(N)]
arr2 =[list(map(int, input().split())) for _ in range(N)]
arr3 =[[1 if arr1[i][j] != arr2[i][j] else 0 for j in range(M)] for i in range(N)]
#새로운 배열을 생성함과 동시에 arr1과 arr2 배열의 같음 여부를 담음. 
#조건: 1 if 조건 else 0은 조건이 참이면 1 아니면 0을 넣어라라는 문법. 암기해라 걍.
#j 부분만 괄호 안에 넣은 이유:가로줄(한줄에 들어갈 칸의 개수)을 우선 만든후 세로줄로 쌓기

for row in arr3:
    for elem in row:
        print(elem, end=" ")
    print() #다음줄로 넘어가라는 역할