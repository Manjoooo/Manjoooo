inp = input()
arr = inp.split()

te1 = int(arr[0])
te2 = int(arr[1])

if te1 >= 90 and te2 >= 95:
    print("100000")
elif te1 >= 90 and te2 >= 90:
    print("50000")
else:
    print("0")