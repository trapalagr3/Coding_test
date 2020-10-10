n,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
# 정렬
A.sort()
B.sort(reverse=True)


for i in range(k):
    print(i)
    if A[i] < B[i]:
        A[i],B[i] = B[i],A[i]
    else:
        break
print(sum(A))