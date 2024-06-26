<<<<<<< HEAD
'''
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

N = 7인 경우에 다음과 같은 상담 일정표를 보자.

 	1일	2일	3일	4일	5일	6일	7일
Ti	3	5	1	1	2	4	2
Pi	10	20	10	20	15	40	200

1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 
5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.

상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 
예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다. 
2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.
또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.

퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 
이때의 이익은 10+20+15=45이다.

상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.
'''

import sys
input=sys.stdin.readline
n=int(input().rstrip())
dp=[0]*(n+1) # i번째 날 부터 마지막 날까지 낼 수 있는 최대 이익
t=[] # time
p=[] # pay
max_val=0

for _ in range(n):
    x,y=map(int, input().rstrip().split())
    t.append(x)
    p.append(y)

# 뒤에서부터, 거꾸로
for i in range(n-1,-1,-1): 
    time=t[i]+i
    
    # 상담이 기간 안에 끝나는 경우
    if time<=n:
        # 현재까지의 최고의 이익 계산
        dp[i]=max(p[i]+dp[time], max_val) # 현재 상담 일자 + 현재 상담을 마친 일자부터 최대 이윤
        max_val=dp[i]
    
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i]=max_val
    
=======
'''
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

N = 7인 경우에 다음과 같은 상담 일정표를 보자.

 	1일	2일	3일	4일	5일	6일	7일
Ti	3	5	1	1	2	4	2
Pi	10	20	10	20	15	40	200

1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 
5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.

상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 
예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다. 
2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.
또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.

퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 
이때의 이익은 10+20+15=45이다.

상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.
'''

import sys
input=sys.stdin.readline
n=int(input().rstrip())
dp=[0]*(n+1) # i번째 날 부터 마지막 날까지 낼 수 있는 최대 이익
t=[] # time
p=[] # pay
max_val=0

for _ in range(n):
    x,y=map(int, input().rstrip().split())
    t.append(x)
    p.append(y)

# 뒤에서부터, 거꾸로
for i in range(n-1,-1,-1): 
    time=t[i]+i
    
    # 상담이 기간 안에 끝나는 경우
    if time<=n:
        # 현재까지의 최고의 이익 계산
        dp[i]=max(p[i]+dp[time], max_val) # 현재 상담 일자 + 현재 상담을 마친 일자부터 최대 이윤
        max_val=dp[i]
    
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i]=max_val
    
>>>>>>> 17e683aa9364eb3dd87621d5db424444bb5fd069
print(max_val)