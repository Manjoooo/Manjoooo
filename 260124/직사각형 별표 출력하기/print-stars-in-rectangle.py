inp = input()
arr = inp.split()
n = int(arr[0])
m = int(arr[1])

for i in range(n):
    for j in range(m):
        print("*", end = " ")
    print()