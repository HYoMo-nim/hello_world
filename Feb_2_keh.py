# No. 11399 ATM -------------------------------

n=int(input())

arr=[]
arr=list(map(int, input().split(" ")))

arr.sort()
sum=0

for i in range(n):
    for j in range(i):
        sum+=arr[j]
    sum+=arr[i]

print(sum)


# No. 11047 동전0 -------------------------------

n, k=map(int, input().split(" "))
arr=[]

for i in range(n):
    arr.append(int(input()))

result=0
arr.sort(reverse=True)

for i in arr:
    if i<=k:
        result+=k//i
        k=k%i

print(result)


# No. 1920 수 찾기 -------------------------------

import heapq
# priority queue를 위해 사용. 대충... 들어온 원소를 무조건 오름차순 정렬해서 저장해두는 큐
# heapq.heappush(heap, object):heap에 object(원소) 추가
# heapq.heappop(heap): heap에서 가장 작은 원소(첫 번째로 위치한 원소) 반환
# heapq.heapify(list): list를 즉시 heap으로 변환
# heapq는 리스트를 최소힙으로 다룰 수 있도록 도와줘서 선언할 때 그냥 빈 리스트 선언해주면 편하게 쓸 수 있음
import sys
input=sys.stdin.readline  # 시간초과 뜨길래...

n, k=map(int, input().split())
arr=list(map(int, input().split()))

que=[]

for i in arr:
    heapq.heappush(que, i)
    if len(que)>k:
        print(heapq.heappop(que), end=' ')

while que:
    print(heapq.heappop(que), end=' ')

