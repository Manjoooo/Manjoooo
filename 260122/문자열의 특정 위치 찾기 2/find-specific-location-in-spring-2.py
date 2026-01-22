eng = ["apple", "banana", "grape", "blueberry", "orange"]

a = input()

cnt = 0

for i in range(5):
    if eng[i][2] == a or eng[i][3] == a:
        print(eng[i])
        cnt += 1

print(cnt)

#eng[i][2]는 grape에 대해서 한글자 한글자가 맞는지를 보는 과정임.
#for문을 함으로써 하나하나 변환하여 단어가 맞는 것인지 확인하는 것임. 