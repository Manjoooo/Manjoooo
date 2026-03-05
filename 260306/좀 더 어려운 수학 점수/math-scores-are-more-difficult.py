inp1 = input()
arr1 = inp1.split()
a_math, a_eng = int(arr1[0]), int(arr1[1])

inp2 = input()
arr2 = inp2.split()
b_math, b_eng = int(arr2[0]), int(arr2[1])

# 출력
if a_math > b_math or (a_math == b_math and a_eng > b_eng):
    print("A")
else:
    print("B")

#데이터가 들어오는 줄 수에 맞춰서 입력을 각각 받았기 때문에