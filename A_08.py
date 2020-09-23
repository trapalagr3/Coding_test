## 내가 만든 코드 ##
# S = input()
# Str,Int = [],[]
# result = ''
# for s in S:
#     try:
#         Int.append(int(s))
#     except:
#         Str.append(s)
# Str.sort()
# Int.sort()
#
# for i in range(len(Str)):
#     result+=Str[i]
# result += str(sum(Int))
# print(result)

## 책 정답 코드 ##

data = input()
result = []
value = 0

for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)
result.sort()

# 숫자가 있으면 문자 뒤에 삽입
if value != 0:
    result.append(str(value))
# 최종 결과 출력
#print(result)
print(''.join(result))
