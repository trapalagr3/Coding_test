n = int(input())
data = []
for i in range(n):
    temp = input().split()
    data.append((temp[0],int(temp[1])))
data = sorted(data, key = lambda data: data[1])

# 출력
for i in data:
    print(i[0], end = ' ')