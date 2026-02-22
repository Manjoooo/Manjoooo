inp = input()
arr = inp.split(":")
h = int(arr[0])
m = int(arr[1])
#시간과 분을 나누기 위해서 inp.split 과정이 필요한것 
# 출력
print(f"{h + 1}:{m}")