'''
채굴자가 얻을 수 있는 금의 최대 금의 크기

m번 이동 - 오른쪽 위, 오른쪽, 오른쪽 아래
'''

import sys
input=sys.stdin.readline
t=int(input().rstrip())

for _ in range(t):
    total=0
    n, m=map(int, input().rstrip().split())

    gold=list(map(int, input().rstrip().split()))
    # gold=[gold[i*m:i*m+m] for i in range(n)]
    #[[gold[i*m+j] for i in range(n)] for j in range(m)]
        
    # 다이나믹 프로그래밍은 dp라는 새로운 table 초기화하여 사용
    dp=[gold[i*m:i*m+m] for i in range(n)]
    
    # 1열 gold중 max + 2열 gold -> 2열 gold중 max + 3열 gold -> 3열 gold중 max + 4열 gold   
    for j in range(1,m): # 1,2,3, .. m-1열
        for i in range(n):
            # 왼쪽 위에서 오는 것
            if i==0:
                left_up=0 # 0행은 왼쪽 위에서 오는 것 x
            else:
                left_up=dp[i-1][j-1]
        
            # 왼쪽 아래에서 오는 경우
            if i==n-1:
                left_down=0
            else:
                left_down=dp[i+1][j-1]
            
            # 왼쪽에서 오는 경우
            left=dp[i][j-1]
        
            dp[i][j]=dp[i][j]+max(left_up, left, left_down)
    
    result=0
    for i in range(n):
        result=max(result, dp[i][m-1])
    
    print(result)
