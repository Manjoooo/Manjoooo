inp1 = input()
arr1 = inp1.split()
a_age, a_sex = int(arr1[0]), arr1[1]

inp2 = input()
arr2 = inp2.split()
b_age, b_sex = int(arr2[0]), arr2[1]

if (a_age >= 19 and a_sex == "M") or (b_age >= 19 and b_sex == "M"):
    print("1")
else:
    print("0")