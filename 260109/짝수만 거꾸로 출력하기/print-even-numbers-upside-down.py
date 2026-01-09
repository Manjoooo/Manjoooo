n = int(input()) # 정수 n개 입력.

arr= list(map(int, input().split())) # 주어진 수를 배열을 구현함.
#순서가 반영되어야 하기 때문에 list 구현은 필

for i in range(n-1, -1, -1): #range(시작, 끝, 간격) 인덱스 0부터 시
    if arr[i] % 2 == 0:
        print(arr[i], end=" ")