inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])

inv = input()
ars = inv.split()

c = int(ars[0])
d = int(ars[1])

if a > c and b > d:
    print("1")
else:
    print("0")