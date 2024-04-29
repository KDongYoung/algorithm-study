<<<<<<< HEAD
'''
맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 
범위는 0 이상 9999 이하이다.
'''

import sys
input=sys.stdin.readline
n=int(input().rstrip())

total=0
triangle=[list(map(int, input().rstrip().split())) for _ in range(n)]

# 다이나믹 프로그래밍은 dp라는 새로운 table 초기화하여 사용
dp=triangle

# i행 j열: i행 j열 + max(i-1행 j-1열, i-1행 j열)
for i in range(1,n): # 1,2,3, .. m-1열
    for j in range(i+1):
        # 왼쪽 위에서 오는 것
        if j==0:
            left_up=0 # 0행은 왼쪽 위에서 오는 것 x
        else:
            left_up=dp[i-1][j-1]
    
        # 오른쪽 위에서 오는 경우
        if j==i:
            right_up=0
        else:
            right_up=dp[i-1][j]
        
        dp[i][j]=dp[i][j]+max(left_up, right_up)

result=max(dp[n-1])
=======
'''
맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 
범위는 0 이상 9999 이하이다.
'''

import sys
input=sys.stdin.readline
n=int(input().rstrip())

total=0
triangle=[list(map(int, input().rstrip().split())) for _ in range(n)]

# 다이나믹 프로그래밍은 dp라는 새로운 table 초기화하여 사용
dp=triangle

# i행 j열: i행 j열 + max(i-1행 j-1열, i-1행 j열)
for i in range(1,n): # 1,2,3, .. m-1열
    for j in range(i+1):
        # 왼쪽 위에서 오는 것
        if j==0:
            left_up=0 # 0행은 왼쪽 위에서 오는 것 x
        else:
            left_up=dp[i-1][j-1]
    
        # 오른쪽 위에서 오는 경우
        if j==i:
            right_up=0
        else:
            right_up=dp[i-1][j]
        
        dp[i][j]=dp[i][j]+max(left_up, right_up)

result=max(dp[n-1])
>>>>>>> 17e683aa9364eb3dd87621d5db424444bb5fd069
print(result)