# 위에서 아래로
# 숫자 입력
n = int(input())
# 숫자 입력
array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)
# array = sorted(array,reverst=True)
for i in range(n):
    print(array[i],end=' ')
# for i in array:
    print(i,end='')