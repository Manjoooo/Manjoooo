inp = input()
arr = inp.split()
n = int(arr[0])
a = int(arr[1])

i=1
while i <= n:
    if i % a == 0:
     print(1)
    else:
        print(0)
    i+=1

#while문은 1을 더해주지 않으면 그 값 그대로 나오니까 주의