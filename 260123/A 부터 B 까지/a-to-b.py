
inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])
i = a

while i <= b:
    print(i, end=" ")
    if i % 2 == 1:
        i *= 2
    else:
        i += 3

#i를 a라고 지정한건 처음 값을 보존하기 위해서임. 
