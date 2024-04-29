'''
못생긴 수: 2,3,5 만을 소인수로 가지는 수 / 2,3,5를 약수로 가지는 합성수
n번째 못생긴 수를 구하시오.
'''
import sys

input=sys.stdin.readline
n=int(input().rstrip())
# ugly=[0]*n
# ugly[0]=1 # 첫번째 못생긴 수 = 1

# i2=i3=i5=0 # 인덱스
# next2,next3,next5=2,3,5 # 다음으로 다뤄야하는 곱셈 값

# for l in range(1,n): # [1, 다음부터 확인]
#     # 다음으로 다뤄야하는 곱셈 값들 중 최솟값을 l번째 인덱스에 저장
#     ugly[l]=min(next2,next3,next5)
    
#     # 인덱스에 따라서 곱셈 결과를 증가
#     # elif로 하면 중복이 존재 ex) 6
#     if ugly[l]==next2:
#         i2+=1 
#         next2=ugly[i2]*2 # 다음을 위해
#     if ugly[l] == next3:
#         i3+=1
#         next3=ugly[i3]*3 # 다음을 위해
#     if ugly[l] == next5:
#         i5+=1
#         next5=ugly[i5]*5 # 다음을 위해

# # n번째 못생긴 수를 출력
# print(ugly[n-1])     

count = 1
data = [1] # 시작 1부터
for i in range(2,1000):
    if count == n:
        print(data[count-1])
        break
    if (i%2 == 0) or (i%3 == 0) or (i%5 == 0):
        count += 1
        data.append(i)
        # data.sort()   