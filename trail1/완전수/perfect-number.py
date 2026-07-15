start, end = map(int, input().split())

perfect_number_count = 0
# Please write your code here.
for num in range(start,end):
    cnt=0
    for i in range(1,num):
        if num % i == 0:
            cnt += i
    
    if cnt == num:
        perfect_number_count += 1


print(perfect_number_count)