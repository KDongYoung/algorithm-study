'''
고정점: 값과 인덱스가 동일한 원소
고정점 최대 1개만 존재
고정점 없으면 -1 출력
'''
import sys

def bs(element, s,e):
    
    if s>e:  # while s<e: 느낌
        return None
    
    mid=(s+e)//2

    if element[mid]==mid:
        return mid
    elif element[mid]>mid:
        return bs(element, s, mid-1)
    else:
        return bs(element, mid+1, e)

if __name__ == "__main__":
    input=sys.stdin.readline
    
    n=int(input().rstrip())    
    element=list(map(int, input().rstrip().split()))
    
    idx=bs(element, 0, len(element)-1)
    
    if idx==None:
        print(-1)
    else:
        print(idx)
    
    # 만약에 고정점이 여러개였다면, '정렬된 배열에서 특정 정수의 개수 구하기' 문제 처럼 처음과 끝을 구한다면 된다.