<<<<<<< HEAD
'''
N명의 병사가 무작위로 나열되어 있다. 각 병사는 특정한 값의 전투력을 보유하고 있으며, 
병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 한다. 
다시 말해 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 한다.

또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용한다. 
그러면서도 남아있는 병사의 수가 최대가 되도록 하고 싶다.

예를 들어, N=7일 때 나열된 병사들의 전투력이 다음과 같다고 가정하자.
이 때 3번 병사와 6번 병사를 열외시키면, 다음과 같이 남아있는 병사의 수가 내림차순의 형태가 되며 5명이 된다. 
이는 남아있는 병사의 수가 최대가 되도록 하는 방법이다.

병사에 대한 정보가 주어졌을 때, 남아있는 병사의 수가 최대가 되도록 하기 위해서 
열외해야 하는 병사의 수를 출력하는 프로그램을 작성하시오.
'''

## 이해가 잘 안됨,,,,
import sys
input=sys.stdin.readline
n=int(input().rstrip())
soldier=list(map(int, input().rstrip().split()))
soldier.reverse() # 순서를 뒤집어서 '가장 긴 증가하는 부분 수열 문제로 변환

dp=[1]*n
for i in range(1,n):
    for j in range(0,i):
        
        if soldier[j] < soldier[i]:
            print(dp[i], dp[j]+1)
            dp[i]=max(dp[i], dp[j]+1)

print(n-max(dp))
=======
'''
N명의 병사가 무작위로 나열되어 있다. 각 병사는 특정한 값의 전투력을 보유하고 있으며, 
병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 한다. 
다시 말해 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 한다.

또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용한다. 
그러면서도 남아있는 병사의 수가 최대가 되도록 하고 싶다.

예를 들어, N=7일 때 나열된 병사들의 전투력이 다음과 같다고 가정하자.
이 때 3번 병사와 6번 병사를 열외시키면, 다음과 같이 남아있는 병사의 수가 내림차순의 형태가 되며 5명이 된다. 
이는 남아있는 병사의 수가 최대가 되도록 하는 방법이다.

병사에 대한 정보가 주어졌을 때, 남아있는 병사의 수가 최대가 되도록 하기 위해서 
열외해야 하는 병사의 수를 출력하는 프로그램을 작성하시오.
'''

## 이해가 잘 안됨,,,,
import sys
input=sys.stdin.readline
n=int(input().rstrip())
soldier=list(map(int, input().rstrip().split()))
soldier.reverse() # 순서를 뒤집어서 '가장 긴 증가하는 부분 수열 문제로 변환

dp=[1]*n
for i in range(1,n):
    for j in range(0,i):
        
        if soldier[j] < soldier[i]:
            print(dp[i], dp[j]+1)
            dp[i]=max(dp[i], dp[j]+1)

print(n-max(dp))
>>>>>>> 17e683aa9364eb3dd87621d5db424444bb5fd069
    