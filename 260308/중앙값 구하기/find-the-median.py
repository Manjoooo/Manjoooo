inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

# 세 값을 리스트에 담습니다.
new_list = [a, b, c]

# 크기 순으로 정렬합니다. (작은 값 -> 중간 값 -> 큰 값)
new_list.sort()

# 정렬된 리스트에서 두 번째(index 1) 값이 바로 우리가 찾는 중앙값입니다.
median = new_list[1]

print(median)