# N,M,K를 공백으로 구분하여 입력받기
n,m,k = map(int,input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0
# 방법 1
while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0:
            break
        result += first
        m -=1 #더할 때마다 1씩 빼기
    if m == 0:
        break
    result += second #두 번째로 큰 수를 한 번 더하기
    m -=1

# 방법 2
# 가장 큰수가 더해지는 횟수 계산산count = (m//(k+1))*k
count += m % (k+1)

result += (count)* first # 가장 큰 수 더하기
result += (m-count) * second

print(result) # 최종 답안 출력