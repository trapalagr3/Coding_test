## 내가 만든 코드 ##
N = input()# 현재 캐릭터 점수
leng = len(N)
head,tail = 0,0
for i in range(leng):
    if i<int(leng/2):
        head += int(N[i])
    else:
        tail += int(N[i])
if head == tail:
    print('LUCKY')
else:
    print('READY')
## 교재 답안 코드 ##

# N = input()
# length = len(N) # 점수값의 총 자릿수
# summary = 0
# # 왼쪽 부분의 자릿수 합 더하기
# for i in range(length//2):
#     summary += int(n[i])
# for i in range(length//2,length):
#     summary -= int(n[i])
# if summary == 0: print("LUCKY")
# else: print("READY")

